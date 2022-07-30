import requests

new_user ={
    "userId": '10',
    "title": '  Testing  ',
    "body": '  New  '
}

def get(url):
   response= requests.get(url)
   print("Status for GET ",url,response)

   try:
       assert response.status_code == 200
   except:
       print("Not Found")



def post(url):
    response =requests.post(url, json=new_user)
    print("Status for POST",url,response)
    try:
        assert response.status_code == 201
    except:
        print("Not Found")
    json_response = response.json()
    print(json_response)

def delete(url):
    response =requests.delete(url)
    print("Status for DELETE ",url,response)
    content_response = response.content
    print(content_response)
    try:
        assert response.status_code == 200

    except :
        print('Not Found')

#First_case
GET_All_Posts= "https://jsonplaceholder.typicode.com/posts"
get(GET_All_Posts)

#Second_case
GET_Post_By_Id="https://jsonplaceholder.typicode.com/posts/1"
get(GET_Post_By_Id)

#Third_case
GET_Comments_BY_Id="https://jsonplaceholder.typicode.com/comments?postId=1"
get(GET_Comments_BY_Id)

#Fourth_case
POST_New_Id="https://jsonplaceholder.typicode.com/posts"
post(POST_New_Id)

#Fifth_case
DELETE_By_Id="https://jsonplaceholder.typicode.com/posts/1"
delete(DELETE_By_Id)

#Negative_for_GET
GET_Post_By_Id_Negative ="https://jsonplaceholder.typicode.com/posts/500"
get(GET_Post_By_Id_Negative)

#Negative_for_delete 
DELETE_By_Id_Negative = "https://jsonplaceholder.typicode.com/posts/-1"
delete(DELETE_By_Id_Negative)