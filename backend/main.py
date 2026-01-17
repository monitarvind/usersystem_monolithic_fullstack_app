from fastapi import FastAPI, HTTPException, Path, Query
from fastapi.responses import JSONResponse
import json
from pydantic_data import User_system

app = FastAPI()

#User Data Loader Function
def userdata_list():
    with open('../db/userlist.json', 'r') as udl:
        data = json.load(udl)
    return data

#User Data Saver Function
def save_userdata(data):
    with open('../db/userlist.json', 'w') as sud:
        json.dump(data, sud, indent=2, default=str)

#API Endpoints:

#Route 1: Landing Page
@app.get("/")
def landing_page():
    return {"message": "Welcome to the User System API"}

#Route 2: Homepage
@app.get("/homepage")
def homepage():
    return {"This is a homepage of User Management System.\n The objective is to manage the users via a chatbot and user information is stored in a DB.\n "}

#Route 3: All User List
@app.get("/all_user_list")
def all_user_list():
    data = userdata_list()
    return data


#Route 4: Create User
@app.post("/create_user")
def create_user(user_details: User_system):
    #loading the pre-existing data
    data = userdata_list()

    if user_details.id in data:
        raise HTTPException(status_code=400, detail='User ID already exists')
    
    data[user_details.id] = user_details.model_dump(exclude={'id'})
    
    #save updated data back to file
    save_userdata(data)
   
    return f"User Added Successfully: {user_details}"

#Route 5: Fetch User Details on the basis of User ID
@app.get("/user_details/{user_id}")
def user_details(user_id: str = Path(..., description = 'ID of the user', example = "001")):
    data = userdata_list()
    if user_id in data:
        return data[user_id]
    else:
        raise HTTPException(status_code=404, detail="User not found")
#=========================================================================================
# #Created with Abhinit
# @app.get("/user_details/{user_id}")
# def user_details(user_id: str):
#     data = userdata_list()
#     print(data)
#     print(data[user_id])
# #    print(data.key)
#     return data[user_id]
    
#=========================================================================================
#Route 6: Update User on the basis of User ID

@app.put("/update_user/{user_id}")
def update_user(user_id: str, field: str = Query(..., description='Field to update: married, weight, phone, emergency_contact'), new_value: str = Query(...)):
    data = userdata_list()
    
    if user_id not in data:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_data = data[user_id]
    field = field.lower()
    
    if field not in user_data:
        raise HTTPException(status_code=400, detail=f"Invalid field. Choose from: {list(user_data.keys())}")
    
    # Convert value based on field type
    if field == "married":
        data[user_id][field] = new_value.lower() == "true"
    elif field == "weight":
        data[user_id][field] = float(new_value)
    elif field == "emergency_contact":
        data[user_id][field] = int(new_value) if new_value else None
    else:
        data[user_id][field] = new_value
    
    save_userdata(data)
    return JSONResponse(status_code=200, content={"message": f"User {user_id} updated successfully", "field": field, "new_value": data[user_id][field]})

# #Route 7: Delete User on the basis of User ID
@app.delete("/delete_user/{user_id}")
def delete_user(user_id: str):
    data = userdata_list()
    
    if user_id in data:
        del data[user_id]

    else:
        raise HTTPException(status_code=404, detail=f"User not found: {user_id}")
    save_userdata(data)
    return JSONResponse(status_code=200, content={"message": "User deleted successfully."})

#Route 8: Query Parameters i.e. sorting 
@app.get("/sorting")
def sort_users(sort_by: str = Query(..., description = "Sort by dob or phone"), order: str = Query("asc", description= "sort in asc or desc order") ):
    
    valid_option = ["dob", "phone"]

    if sort_by not in valid_option:
        raise HTTPException(status_code=400, detail=f"Invalid option. Choose from {valid_option}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid. Select asc or desc")

    data = userdata_list()

    reverse_order = order == 'desc'

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=reverse_order)

    return sorted_data


#Route 9: Login for authentication

    