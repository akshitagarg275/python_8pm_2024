import helper


def main():
    run = 1
    helper.create_table()

    while run :
        print("Press 1 : To add data")
        print("Press 2 : To read data")
        print("Press 3 : To update data")
        print("Press 4 : To delete data")
        print("Press 5 : To exit")

        ch =  input("********* Enter your choice ********")

        if ch == '1':
            todo = input("Enter the todo: ")
            helper.add_todo(todo)
        elif ch == '2':
            helper.read_todos()
        elif ch == '3':
            idx = int(input("Enter todo id to be updated: "))
            update_todo = input("Enter new todo: ")
            helper.update_todo(idx,update_todo)
        elif ch == '4':
            pass
        elif ch == '5':
            run = 0
    
    helper.close_connection()




if __name__ == '__main__':
    main()