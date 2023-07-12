```JSON
{
    "user": {
        "username": "staff",
        "email": "staff@staff.com",
        "password": "staff",
        "usertype": "staff"
    },
    "name": "John",
    "surname": "Doe",
    "address": "123 Main Street",
    "telephone1": "555-1234",
    "telephone2": "555-5678",
    "dateofbirth": "1990-01-01",
    "nicnumber": "123456789V",
    "branch": "Sewanapitiya",
    "is_collector": false
}


  {
    "user": {
      "username": "customer",
      "email": "customer@customer.com",
      "password": "customer",
      "usertype": "customer"
    },
    "name": "Jane",
    "surname": "Wotson",
    "address": "123 Main St",
    "telephone1": "555-1234",
    "telephone2": "555-5678",
    "dateofbirth": "1990-01-01T00:00:00Z",
    "nicnumber": "1234567890"
  }


  {
  "username": 1,
  "loaned_date": "2022-07-15",
  "branch_location": "Polonnaruwa",
  "loaned_amount": 500000.0,
  "bike_number": "AB123",
  "first_guarantor": 1,
  "second_guarantor": 1,
  "loan_period": 12
}



  ```
  
  http://127.0.0.1:8000/customers/getnames - GET method for getting all Customer names and Ids

  http://127.0.0.1:8000/users/staff/add - POST

  http://127.0.0.1:8000/users/customer/add - POST

  http://127.0.0.1:8000/loans/getall - GET method for getting all loans

  http://127.0.0.1:8000/loans/add -- POST method for adding new loans

  http://127.0.0.1:8000/loanvalues/update/ - POST method for updating loanvalues