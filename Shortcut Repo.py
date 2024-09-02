import mysql.connector

def Retrieve_Chrome_Shortcuts_Windows(opt):
    try:
        # Establishing the connection with chrome_windows database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Nikichiki12@',
            database='chrome_windows'
        )
        
        #Checking whether the connection is established or not
        if connection.is_connected():
            #print('Connected to chrome_windows database')
            # Creating a cursor object using the cursor() method
            cursor = connection.cursor()
            # Executing SQL queries
            # Tab & Windows shortcuts
            if opt == 1:        #User wants to see the available tab and window shortcuts
                sql_query = "SELECT task FROM tab_window;"      #task attribute is selected from tab_window table
                cursor.execute(sql_query)

                # Fetching all rows from the result set
                rows = cursor.fetchall()

                # Printing each row
                for row in rows:
                    print(row)

                kw=input("Enter the keyword ")
                query = "SELECT * FROM tab_window WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",)) #the second attribute of the execute method should be a tuple and that value will be substituted in the query statement/ syntax requirement of second parameter of execute method is tuple and by passing parameters as a tuple, you can easily handle multiple parameters of different types
                ans= cursor.fetchall()
                #fetchall method returns a list of tuples containing the values of the attributes
                # Printing each row
                for x in ans:
                    print(x)
                
                #User input for confirming whether he/she wants to retrieve more shortcuts
                qs=input("Want more shortcuts?[yes/no] ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input ")
                   
            # Google Chrome Feature shortcuts        
            elif opt==2:
                sql_query = "SELECT task FROM google_chrome_feature;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

                kw=input("Enter the keyword ")
                query = "SELECT * FROM google_chrome_feature WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)

                qs=input("Want more shortcuts?[yes/no] ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input ")
            
            #Address Bar shortcuts
            elif opt==3:
                sql_query = "SELECT task FROM address_bar;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

                kw=input("Enter the keyword ")
                query = "SELECT * FROM address_bar WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)
                
                qs=input("Want more shortcuts?[yes/no] ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input ")

            #Webpage shortcuts
            elif opt==4:
                sql_query = "SELECT task FROM web_page;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                kw=input("Enter the keyword ")
                query = "SELECT * FROM web_page WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)

                qs=input("Want more shortcuts?[yes/no] ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input ")
            
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")

def Retrieve_Chrome_Shortcuts_MAC(opt):
    try:
        # Establishing the connection with chrome_mac database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Nikichiki12@',
            database='chrome_mac'
        )
        
        if connection.is_connected():
            #print('Connected to chrome_mac database')
            cursor = connection.cursor()
            # Tab & Windows shortcuts
            if opt == 1:
                sql_query = "SELECT task FROM tab_window;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()

                for row in rows:
                    print(row)
                kw=input("Enter the keyword ")
                query = "SELECT * FROM tab_window WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)

                qs=input("Want more shortcuts?[yes/no] ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input ")
                    
            # Google Chrome Feature shortcuts        
            elif opt==2:
                sql_query = "SELECT task FROM google_chrome_feature;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

                kw=input("Enter the keyword ")
                query = "SELECT * FROM google_chrome_feature WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)

                qs=input("Want more shortcuts?[yes/no] ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input ")
            
            #Address Bar shortcuts
            elif opt==3:
                sql_query = "SELECT task FROM address_bar;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                
                kw=input("Enter the keyword ")
                query = "SELECT * FROM address_bar WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)

                qs=input("Want more shortcuts?[yes/no] ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input")
                

            #Webpage shortcuts
            elif opt==4:
                sql_query = "SELECT task FROM webpage;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                
                kw=input("Enter the keyword: ")
                query = "SELECT * FROM webpage WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)

                qs=input("Want more shortcuts?[yes/no]: ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input ")

    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")


def Retrieve_PC_Shortcuts_Windows(opt):
    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Nikichiki12@',
            database='pc_windows'
        )
        
        if connection.is_connected():
            #print('Connected to pc_windows database')
            cursor = connection.cursor()
            # file_explorer shortcuts
            if opt == 1:
                sql_query = "SELECT task FROM general;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()       
                for row in rows:
                    print(row)

                kw=input("Enter the keyword: ")
                query = "SELECT * FROM general WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)

                qs=input("Want more shortcuts?[yes/no]: ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input")
                
            # general shortcuts        
            elif opt==2:
                sql_query = "SELECT task FROM windows_logo_key;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

                kw=input("Enter the keyword: ")
                query = "SELECT * FROM windows_logo_key WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)
                
                qs=input("Want more shortcuts?[yes/no] ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input")
            
            #Settings shortcuts
            elif opt==3:
                sql_query = "SELECT task FROM  file_explorer;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                
                kw=input("Enter the keyword: ")
                query = "SELECT * FROM  file_explorer WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)
                qs=input("Want more shortcuts?[yes/no]: ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input")

            #Window logo key shortcuts
            elif opt==4:
                sql_query = "SELECT task FROM settings;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                
                kw=input("Enter the keyword: ")
                query = "SELECT * FROM settings WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)

                qs=input("Want more shortcuts?[yes/no]: ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input ")
                
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")


def Retrieve_PC_Shortcuts_MAC(opt):
    try:
        # Establishing the connection
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Nikichiki12@',
            database='pc_mac'
        )
        
        if connection.is_connected():
            #print('Connected to pc_mac database')
            cursor = connection.cursor()
            # accessibility shortcuts
            if opt == 1:
                sql_query = "SELECT task FROM general;"
                cursor.execute(sql_query)   
                rows = cursor.fetchall()    
                for row in rows:
                    print(row)
                kw=input("Enter the keyword: ")
                query = "SELECT * FROM general WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)
                
                qs=input("Want more shortcuts?[yes/no]: ")
                if qs=='yes':
                    display_pc_shortcuts_MAC()
                if qs=='no':
                    print("Thank you for using ")
                    pass
                else:
                    display_pc_menu()

            # General shortcuts        
            elif opt==2:
                sql_query = "SELECT task FROM sleep_logout;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

                kw=input("Enter the keyword: ")
                query = "SELECT * FROM sleep_logout WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)
                
                qs=input("Want more shortcuts?[yes/no]: ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input ")
            
            #Sleep_logout shortcuts
            elif opt==3:
                sql_query = "SELECT task FROM accessibility;"
                cursor.execute(sql_query)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
                
                kw=input("Enter the keyword: ")
                query = "SELECT * FROM accessibility WHERE task LIKE %s"
                cursor.execute(query, ( "%" + kw + "%",))
                ans= cursor.fetchall()
                for x in ans:
                    print(x)
                
                qs=input("Want more shortcuts?[yes/no]: ")
                if qs=='yes':
                    display_main_menu()
                elif qs=='no':
                    print("Thank you for using ")
                    exit()
                else:
                    print("Enter valid input 7")
                
    except mysql.connector.Error as e:
        print("Error connecting to MySQL database:", e)

    finally:
        # Closing the connection
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            #print("MySQL connection is closed")

#Main Menu
def display_main_menu():
    print("Welcome to the Centralised Repository for Shortcuts!")
    print("Which shortcuts do you want? ")
    print("1. Chrome Shortcuts")
    print("2. PC Shortcuts")
    print("3. Go Back to start")
    print("4. About")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_chrome_menu()     
    elif choice == '2':
        display_pc_menu()         
    elif choice == '3':
        print()
        display_main_menu()
    elif choice == '4':
        about()
    else:
        print("Invalid choice. Please try again.")

#Operating System Options (Windows or MAC)
def display_chrome_menu():
    print("\nWhich Operating System do you use?")
    print("1. Windows & Linux")
    print("2. MAC")
    print("3. Go back to start")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_chrome_shortcuts_windows()     #Line 523
    elif choice == '2':
        display_chrome_shortcuts_MAC()
    elif choice == '3':
        print()
        display_main_menu()
    else:
        print("Invalid choice. Please try again.")

#Operating System Options(Windows or MAC)
def display_pc_menu():
    print("\nWhich Operating System do you use?")
    print("1. Windows Shortcuts")
    print("2. MAC Shortcuts")
    print("3. Go back to start")
    choice = input("Enter your choice: ")
    if choice == '1':
        display_pc_shortcuts_windows()
    elif choice == '2':
        display_pc_shortcuts_MAC()
    elif choice == '3':
        print()
        display_main_menu()
    else:
        print("Invalid choice. Please try again.")
 
#Displaying available categories of shortcuts for Chrome Windows
def display_chrome_shortcuts_windows():
    print(f"\nCategories of Chrome Shortcuts for Windows you want:")
    print("1. Tab & window shortcuts")
    print("2. Google Chrome feature shortcuts")
    print("3. Address bar shortcuts")
    print("4. Webpage shortcuts")
    print("5. Go back to start")
    print("6. Go back one step")
    choice = input("Enter your choice: ")
    if choice == '1':
        print("Available Tab & Window Shortcuts")
        #Parameterised function which takes choice as input and acts accordingly
        Retrieve_Chrome_Shortcuts_Windows(1)   
    elif choice == '2':
        print("Available Chrome Shortcuts")
        Retrieve_Chrome_Shortcuts_Windows(2)
    elif choice == '3':
        Retrieve_Chrome_Shortcuts_Windows(3)
    elif choice == '4':
        Retrieve_Chrome_Shortcuts_Windows(4)
    elif choice == '5':
        print()
        display_main_menu()
    elif choice == '6':
        print()
        display_chrome_menu()
    else:
        print("Invalid Input")

# Displaying available categories of shortcuts for Chrome MAC
def display_chrome_shortcuts_MAC():
    print(f"\nCategories of Chrome Shortcuts for MAC you want:")
    print("1. Tab & window shortcuts")
    print("2. Google Chrome feature shortcuts")
    print("3. Address bar shortcuts")
    print("4. Webpage shortcuts")
    print("5. Go to start")
    print("6. Go back one step")
    choice = input("Enter your choice: ")
    if choice == '1':
        Retrieve_Chrome_Shortcuts_MAC(1)
        pass
    elif choice == '2':
        Retrieve_Chrome_Shortcuts_MAC(2)
        pass
    elif choice == '3':
        Retrieve_Chrome_Shortcuts_MAC(3)
    elif choice == '4':
        Retrieve_Chrome_Shortcuts_MAC(4)
    elif choice == '5':
        print()
        display_main_menu()
    elif choice == '6':
        print()
        display_chrome_menu()
    else:
        print("Invalid Input")
           
# Displaying available categories of shortcuts for PC Windows
def display_pc_shortcuts_windows():
    print("\nCategories of PC Shortcuts for Windows:")
    print("1. General shortcuts")
    print("2. Windows logo key shortcuts")
    print("3. File explorer shortcuts")
    print("4. Setting shortcuts")
    print("5. Go to start")
    print("6. Go back one step")
    choice = input("Enter your choice: ")
    if choice == '1':
        Retrieve_PC_Shortcuts_Windows(1)
    elif choice == '2':
       Retrieve_PC_Shortcuts_Windows(2)
    elif choice == '3':
        Retrieve_PC_Shortcuts_Windows(3)
    elif choice == '4':
        Retrieve_PC_Shortcuts_Windows(4)
        pass
    elif choice == '5':
        print()
        display_main_menu()
    elif choice == '6':
        print()
        display_pc_menu()
    else:
        print("Invalid input")

# Displaying available categories of shortcuts for Chrome MAC
def display_pc_shortcuts_MAC():
    print("\nCategories of PC Shortcuts for MAC:")
    print("1. General shortcuts")
    print("2. Sleep, log out and shut down shortcuts")
    print("3. Accessibility shortcuts")
    print("4. Go to start")
    print("5. Go back one step")
    choice = input("Enter your choice: ")
    if choice == '1':
        Retrieve_PC_Shortcuts_MAC(1)
    elif choice == '2':
       Retrieve_PC_Shortcuts_MAC(2)
    elif choice == '3':
        Retrieve_PC_Shortcuts_MAC(3)
    elif choice == '4':
        print()
        display_main_menu()
    elif choice == '5':
        print()
        display_pc_menu()
    else:
        print("Invalid choice")

#Displays about the service which the program provides
def about():
    print("Hello and Welcome to the Centralised Repository of shortcuts :)\nHere users can easily find the shortcuts for Chrome Windows or Chrome MAC and PC Windows or PC MAC\nThis service allows non-tech people to easily retrieve their required shortcuts by just selecting some categories and entering any keyword of the shortcut they need\nUltimately shortcuts make our life easier and also saves our time")
    qs=input("Go to use shortcuts?[yes/no]")
    if qs=='yes':
        display_main_menu()
    elif qs=='no':
        exit()
    else:
        print("Enter valid input")
def main():
    display_main_menu()

if __name__ == "__main__":
    main()
