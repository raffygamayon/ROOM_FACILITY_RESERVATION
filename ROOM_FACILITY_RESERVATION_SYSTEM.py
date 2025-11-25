reserve=[]
approved=[]
rejected=[]
facilities=["Auditorium", "Roof Deck", "AVR 1", "AVR 2","Multipurpose Hall", "Quadrangle", "SHS Ground", "MS Ground"]
time=["8:00-9:00am", "9:00-10:00am", "10:00-11:00am","11:00am-12:00nn", "1:00-2:00pm", "2:00-3:00pm", "3:00-4:00pm"]
adminpassword="admin123"

while True:
    print()
    print("--- Facilities Reserversation ---")
    print()
    print("1. Faculty/Student Menu")
    print("2. Admin Staff Menu")
    print("3. Exit")
    print()
    role=input("Choose a number 1-3: ")


    if role == "1":
        while True:
            print()
            print("--- Faculty/Student Menu ---")
            print()
            print("1. View Available Facilities and Time Slots")
            print("2. Submit Reservation Request")
            print("3. View My Reservation Status")
            print("4. Back to Main Menu")
            choice=input("Choose a number 1-4: ")

            if choice == "1": 
                print()
                print("--- Room Facilities ---")
                print()
                facilities = ["Auditorium", "Roof Deck", "AVR 1", "AVR 2", "Multipurpose Hall", "Quadrangle", "SHS Ground", "MS Ground"]
                for a in facilities:
                    print("-", a)
                print()
                print("--- Time ---")
                time = ("8:00-9:00am", "9:00-10:00am", "10:00-11:00am", "11:00am-12:00nn", "1:00-2:00pm", "2:00-3:00pm", "3:00-4:00pm")
                for z in time:
                    print("-", z)

            elif choice == "2":
               print()
               print("--- Submit Reservation Request ---")
               name=input("Name: ").strip()


               while True:
                   print()
                   print("--- Available Facilities ---")
                   print()
                   for x in facilities:
                       print("-", x)

                   print()
                   facility=input("Select Facility: ").strip().lower()
                   print()
 
                   for x in facilities:
                       if x.lower() == facility:
                           x=facility
                           break
                   else:
                         print("Invalid Facility")
                         continue

                   break

               import datetime
               while True:
                    date= input("Date (MM-DD-YYYY): ").strip()

                    try:
                       mm, dd, yyyy = map(int, date.split("-"))
                       enterdate = datetime.date(yyyy, mm, dd)

                       if enterdate < datetime.date.today():
                             print("Invalid! You cannot choose a past date.")
                             continue
 
                    except ValueError:
                           print("Invalid date! Use MM-DD-YYYY and enter a valid date.")
                           continue

                    break

               while True:
                   print()
                   print("--- Available Time Slots ---")
                   print()
                   for o in time:
                       print("-", o)

                   print()
                   times=input("Select Time: ").strip().lower()
                   print()

                   for o in time:
                       if o.lower() == times:
                           o=times
                           break
                   else:
                         print("Invalid Time")
                         continue

                   break

               for y in (reserve + approved):
                   if (y["Name"].lower() == name.lower() and
                       y["Facility"].lower() == x.lower() and 
                       y["Date"].lower() == date.lower() and
                       y["Time"].lower() == o.lower()):
                      
                       print("You already have a resaervation schedule")
                       print("Status:",y["Status"])
                       break

               else:                 
                  print("Reservation Submitted (Pending for Approval).")
                  reserve.append({
                     "Name": name,
                     "Facility": x,
                     "Date": date,
                     "Time": o,
                     "Status":"Pending"
                  })
    
            elif choice == "3":
                print()
                print("--- Check Reservation Status ---")
                findname=input ("Enter your Name: ").strip().lower()
                reservations=reserve+approved+rejected
                found=False

                for q in reservations:
                    found=True
                    if q["Name"].lower() == findname:
                       print()
                       print("--- Reservation Found ---")
                       print()
                       print("Name:", q["Name"])
                       print("Facility:", q["Facility"])
                       print("Date:", q["Date"])
                       print("Time:", q["Time"])
                       print("Status:", q["Status"])
                       print("-----")
                    pass
                if not found:
                    print()
                    print("--- No reservation found ---")
                    print()
                    pass
            elif choice == "4":
                print()
                print("--- Returning to the Main Menu ---")
                break
            else:
                print("--- Invalid Choice. Please Try Again ---")
    
    elif role == "2":
        print()
        password = input("Enter Admin Password: ")
        if password != adminpassword:
            print("--- Incorrect Password ---")
            continue
    
        print()
        print("--- Welcome Admin ---")
        print()

        while True:
            print()
            print("--- ADMIN MENU ---")
            print("1. View and Manage Pending Reservation")
            print("2. View Approved Reservations")
            print("3. Logout")
            print()
 
            admin = input("Choose Number 1-3: ")

            if admin == "1":
                print()
                print("--- PENDING RESERVATIONS ---")
                if not reserve:
                    print()
                    print("--- NO PENDING RESERVATION ---")
                    print()
                else:
                    num = 1
                    for b in reserve:
                     print()
                     print(f"[{num}] Name: {b['Name']}")
                     print(f"    Facility: {b['Facility']}")
                     print(f"    Date: {b['Date']}")
                     print(f"    Time: {b['Time']}")
                     print(f"    Status: {b['Status']}")
                     num += 1
                     print()
                       
                    number =  input("Select A Reservation Number to Approve or Reject: ")
                    if not number.isdigit():
                        print("--- Invalid. Please Try Again ---")
                     
                    elif number == "0":
                        pass
                    else:
                       number = int(number)
                       if 1 <= number <= len(reserve):
                           selected = reserve[number - 1]
                           conflict=False
                           
                           for a in approved:
                               if (a['Facility'].lower() == selected['Facility'].lower() and
                                   a['Date'] == selected['Date'] and
                                   a['Time'].lower() == selected['Time'].lower()):
                                   conflict=True
                           if conflict:
                                   print("---Reservation Rejected---")
                                   print("Time slot is already taken")
                                   selected["Status"] = "Rejected"
                                   rejected.append(selected)
                           else:
                               print("---Reservation Approved Successfully!---")
                               selected["Status"] = "Approved"
                               approved.append(selected)

                           reserve.remove(selected)
                       else:
                           print("Invalid Selection")

            elif admin == "2":
                print("--- APPROVED RESERVATIONS ---")
                if not approved:
                    print("No approved resservation yet")
                else:
                    for p in approved:
                        print("---")
                        print("Name:", p["Name"])
                        print("Facility:", p["Facility"])
                        print("Date:", p["Date"] )
                        print("Time:", p["Time"])
                    print("--- List Ended ---")
                    

            elif admin == "3":
                 print("Logging out from the Admin Menu") 
                 break
            
            else:
                print("Invalid Choice. Please Try Again!")     

    elif role == "3":
        print("Thankyou for using our System!")    
        break
    else:
        print("Invalid Role. Please Try Again!")            