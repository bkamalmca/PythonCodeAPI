# Python Rest API using Flask and Sqlite

The scope of the development module is books wish list to get called through API functions. The API’s to include the add, update, delete and list operations.
The database used for this task is SQLite and Flask for rest API.

### Database table:

CREATE TABLE IF NOT EXISTS wishlist (  
                                        wishlist_id integer PRIMARY KEY,  
                                        user_id text NOT NULL,  
                                        book_id text NOT NULL,  
                                        is_available text  
                                    );

The wishlist_id is the unique identifier for the wishlist transaction, and it is primary_key.
The user_id and book_id is text in this table to demo the purpose and work independently without joins. Otherwise, it will be foreign key to Users and Books tables respectively.
To demo the update use case, the Is_available column is created.

	Y – The book is available in stock to purchase.
 	N – The book is not available in stock to purchase but still can be added to wishlist.

### Python code
The below python code files are created. 
1. Database.py  
 a.	The database related functions are coded in this python file.  
 b.	The sqlite3 library is used and this is better for portable with many databases and utilize the functionality of sql based programming like heavy joins and complex sqls.  
 c.	The functions are created for various operations  


2. Api.py  
      a.	Flask is used to create rest API endpoints.  
      b.	The three endpoints are used  
      i.	/api/wishlist_populate – GET method for onetime to create db, table and populate for demo  
      ii.	/api/wishlist - GET method to list all wishlists data, POST method to insert data to table  
      iii.	/api/wishlist/<wishlist_id> - GET method to list a wishlist data by id, PUT method to update data to table by id, DELETE method to update data to table by id  


3.	Test.py  
a.	To test all the endpoints and methods.   
b.	Run the test.py to run all the test cases. For rerun, comment the test #1 - db create.