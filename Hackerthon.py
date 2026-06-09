list_work = [
    {
        "id": "TS001",
        "name_work": "Thiết kế giao diện app",
        "name_employee": "Nguyễn Văn A",
        "date_think": 10,
        "date_real": 12,
        "index_think_real": 2,
        "status_work": "Cần tăng tốc"
    }
]
def display_work(works):
    if len(works) == 0:
        print("Danh sách công việc hiện đang rỗng")
    else:
        print("--- DANH SÁCH CÔNG VIỆC")
        print(f"{"ID": <5} | {"Tên công việc": <22} | {"Tên nhân viên": <20} | {"Số ngày dự kiến": <5} | {"Số ngày thực tế": <15} | {"Chênh lệch": <5} | {"Trạng thái"}")
        for work in works:
            print(f"{work["id"]: <5} | {work["name_work"]: <20} | {work["name_employee"]: <20} | {work["date_think"]: <15} | {work["date_real"]: <15} | {work["index_think_real"]: <10} | {work["status_work"]}")
def status_employee(date_1,date_2):
    date = date_2 - date_1
    if date < 0:
        return "Hoàn thành sớm"
    elif date == 0:
        return "Bình thường"
    elif date >= 1 and date <= 3:
        return "Cần tăng tốc"
    elif date > 3:
        return "Quá hạn"
def add_work(works):
    id_input = input("Nhập id bạn muốn thêm: ").strip().upper()
    valid = False
    for index,work in enumerate(works):
        if id_input == work.get("id"):
            print("Mã ID bị trùng!")
            valid = True
            break
    if valid == False:
        name_work_input = input("Nhập tên công việc: ").strip()
        name_employee_input = input("Nhập tên nhân viên: ").strip().title()
        date_think_input = input("Nhập ngày dự kiến: ").strip()
        while not date_think_input.isdigit() or int(date_think_input) <= 0:
            print("Số ngày không hợp lệ")
            date_think_input = input("Nhập ngày dự kiến: ").strip()
        date_real_input = input("Nhập ngày thực tế: ").strip()
        while not date_real_input.isdigit() or int(date_real_input) <= 0:
            print("Số ngày không hợp lệ")
            date_real_input = input("Nhập ngày thực tế: ").strip()
        new_work = {
            "id": id_input,
            "name_work": name_work_input,
            "name_employee": name_employee_input,
            "date_think": int(date_think_input),
            "date_real": int(date_real_input),
            "index_think_real": int(date_real_input) - int(date_think_input),
            "status_work": status_employee(int(date_think_input),int(date_real_input))
        }
        works.append(new_work)
        print("Thêm công việc thành công")
def update_list(works):
    id_input = input("Nhập id công việc cần cập nhật: ").strip().upper()
    valid = False
    for index,work in enumerate(works):
        if work.get("id") == id_input:
            date_real_input = input("Nhập ngày thực tế cần cập nhật: ").strip()
            while not date_real_input.isdigit() or int(date_real_input) <= 0:
                print("Số ngày không hợp lệ")
                date_real_input = input("Nhập ngày thực tế cần cập nhật: ").strip()
            work["date_real"] = int(date_real_input)
            work["status_work"] = status_employee(int(work["date_think"]),int(date_real_input))
            print("Cập nhật thành công")
            valid = True
            break
    if valid == False:
        print("ID không tồn tại")
def delete_work(works):
    id_input = input("Nhập ID công việc bạn muốn xóa: ").strip().upper()
    valid = False
    for index,work in enumerate(works):
        if work.get("id") == id_input:
            valid = True
            confirm = input("Bạn có chắc muốn xóa công việc này khỏi dự án không(y/n): ").strip().lower()
            if confirm == "y":
                works.pop(index)
                print("Đã xóa công việc thành công")
                break
            elif confirm == "n":
                print("Đã hủy thao tác")
                break
            else:
                print("Lựa chọn không hợp lệ")
                break
    if valid == False:
        print("ID không tồn tại")
def search_work(works):
    print()
    choice_input = input("""1. Tìm kiếm theo mã TS
2. Tìm kiếm theo tên nhân viên
Chọn chức năng: """).strip()
    if choice_input  == "1":
        search_input = input("Nhập mã TS cần tìm: ").strip().upper()
        print("---Danh sách tìm kiếm---")
        count = 0
        for work in works:
            if search_input in work.get("id"):
                print(f"{work["id"]: <5} | {work["name_work"]: <20} | {work["name_employee"]: <20} | {work["date_think"]: <15} | {work["date_real"]: <15} | {work["index_think_real"]: <10} | {work["status_work"]}")
                count +=1
        if count == 0:
            print("Không tìm thấy kết quả")
    elif choice_input == "2":
        search_input = input("Nhập tên nhân viên cần tìm: ").strip().lower()
        print("---Danh sách tìm kiếm---")
        count = 0
        for work in works:
            if search_input in work.get("name_employee").lower():
                print(f"{work["id"]: <5} | {work["name_work"]: <20} | {work["name_employee"]: <20} | {work["date_think"]: <15} | {work["date_real"]: <15} | {work["index_think_real"]: <10} | {work["status_work"]}")
                count +=1
        if count == 0:
            print("Không tìm thấy kết quả")
    else:
        print("Lựa chọn không hợp lệ")
def digi_work(works):
    count_som = 0
    count_normal = 0 
    count_if_fast = 0
    count_fail = 0
    for work in works:
        if work.get("status_work") == "Hoàn thành sớm":
            count_som += 1 
        elif work.get("status_work") == "Bình thường":
            count_normal += 1
        elif work.get("status_work") == "Cần tăng tốc":
            count_if_fast += 1
        elif work.get("status_work") == "Quá hạn":
            count_fail += 1
    print(f"""---Danh sách thống kê---
Hoàn thành sớm: {count_som}
Bình thường: {count_normal}
Cần tăng tốc: {count_if_fast}
Quá hạn: {count_fail}
    """)
def main():
    while True:
        choose = input("""--- QUẢN LÝ NHÂN VIÊN --- 
1. Hiển thị danh sách công việc 
2. Thêm công việc mới
3. Cập nhật tiến độ thực tế
4. Xóa công việc khỏi dự án
5. Tìm kiếm trên công việc
6. Thống kê trạng thái tiến độ
7. Phân loại tiến độ tự động
8. Thoát chương trình
Chọn chức năng (1-8): """).strip()
        if choose == "1":
            display_work(list_work)
            print()
        elif choose == "2":
            add_work(list_work)
            print()
        elif choose == "3":
            update_list(list_work)
            print()
        elif choose == "4":
            delete_work(list_work)
            print()
        elif choose == "5":
            search_work(list_work)
            print()
        elif choose == "6":
            digi_work(list_work)
            print()
        elif choose == "7":
            print("Chương trình kết thúc")
            break
        else:
            print("Lựa chọn không hợp lệ")
            print()
main()