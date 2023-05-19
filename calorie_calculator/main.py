import tkinter as tk
from data import data_food

selected_items = []
# ฟังก์ชันคำนวณแคลอรี่ที่ควรได้รับตามอายุและเพศ
def calculate_daily_calorie(age, gender):
    if age >= 2 and age <= 3:
        if gender == "ชาย":
            return 1000
        elif gender == "หญิง":
            return 1000
    elif age >= 4 and age <= 8:
        if gender == "ชาย":
            return 1400
        elif gender == "หญิง":
            return 1200
    elif age >= 9 and age <= 13:
        if gender == "ชาย":
            return 1800
        elif gender == "หญิง":
            return 1600
    elif age >= 14 and age <= 18:
        if gender == "ชาย":
            return 2200
        elif gender == "หญิง":
            return 1800
    elif age >= 19 and age <= 30:
        if gender == "ชาย":
            return 2400
        elif gender == "หญิง":
            return 2000
    elif age >= 31 and age <= 50:
        if gender == "ชาย":
            return 2200
        elif gender == "หญิง":
            return 1800
    elif age >= 51:
        if gender == "ชาย":
            return 2000
        elif gender == "หญิง":
            return 1600

# ฟังก์ชันเพิ่มอาหารและแคลอรี่


#ฟังก์ชันเปรียบเทียบอายุและเพศ
def age_gender():
    age = int(age_variable.get().split("-")[0])
    gender = gender_variable.get()
    daily_calorie = calculate_daily_calorie(age, gender)  # คำนวณแคลอรี่ที่ควรได้รับตามอายุและเพศ
    daily_calories.set(daily_calorie)  # กำหนดค่าแคลอรี่ที่ควรได้รับต่อวันให้กับตัวแปร daily_calories

def search_items():
    keyword = entry.get()
    matched_items = [item for item in data_food if keyword in item]
    listbox.delete(0, tk.END)
    for item in matched_items:
        listbox.insert(tk.END, item)

def add_item():
    selected_item = listbox.get(tk.ACTIVE)
    selected_items.append(selected_item)
    update_selected_foods()

def update_selected_foods():
    listbox2.delete(0, tk.END)
    for selected_item in selected_items:
        listbox2.insert(tk.END, selected_item)


def calculate_total():
    age = int(age_variable.get().split("-")[0])
    gender = gender_variable.get() 
    daily_calorie = calculate_daily_calorie(age, gender)
    daily_calories.set(daily_calorie)
    total_cal = sum(data_food[item] for item in selected_items)
    summary= daily_calorie-total_cal
    result_label.config(text=f"แคลอรี่ที่ควรได้รับ: {daily_calorie} แคลอรี่ที่กินไป: {total_cal} แคลอรี่ที่ต้องการเพิ่ม: {summary}")

# GUI
window = tk.Tk()
window.title("โปรแกรมคำนวณแคลอรี่ที่ควรได้รับในแต่ละวัน")
window.geometry("1920x1080")


# ส่วนกรอกเพศและอายุ
age_label = tk.Label(window, text="อายุ:")
age_label.pack()
age_options = ["2-3 ปี", "4-8 ปี", "9-13 ปี", "14-18 ปี", "19-30 ปี", "31-50 ปี", "51 ปีขึ้นไป"]
age_variable = tk.StringVar(window)
age_variable.set(age_options[0])
age_dropdown = tk.OptionMenu(window, age_variable, *age_options)
age_dropdown.pack()

gender_label = tk.Label(window, text="เพศ:")
gender_label.pack()
gender_variable = tk.StringVar(window)
gender_variable.set("ชาย")
gender_radio_male = tk.Radiobutton(window, text="ชาย", variable=gender_variable, value="ชาย")
gender_radio_female = tk.Radiobutton(window, text="หญิง", variable=gender_variable, value="หญิง")
gender_radio_male.pack()
gender_radio_female.pack()

#ปุ่มดูปริมาณcalที่ควรได้รับในแต่ละวัน แปรผันตามเพศและอายุ
button=tk.Button(window, text="คำนวณ", command=age_gender)
button.pack()
daily_calories = tk.IntVar()
daily_calories_label = tk.Label(window, text="แคลอรี่ที่ควรได้รับต่อวัน:")
total_calories_entry = tk.Entry(window, textvariable=daily_calories, state="readonly")
daily_calories_label.pack()
total_calories_entry.pack()

# ส่วนเพิ่มอาหาร
search_frame = tk.Frame(window)
search_label = tk.Label(search_frame, text="พิมพ์คำที่ต้องการค้นหา:")
search_label.pack(side=tk.LEFT)
entry = tk.Entry(search_frame, width=30)
entry.pack(side=tk.LEFT)
search_button = tk.Button(search_frame, text="ค้นหา", command=search_items)
search_button.pack(side=tk.LEFT)
search_frame.pack(pady=10)

# ส่วนรายการ
listbox = tk.Listbox(window, width=50)
listbox.pack(pady=5)


add_button = tk.Button(window, text="เพิ่มรายการ", command=add_item)
add_button.pack(pady=5)

listbox2 = tk.Listbox(window,width=50)
listbox2.pack(pady=10)


result_label = tk.Label(window, text="แคลอรี่ทั้งหมด: ")
result_label.pack()

total_button = tk.Button(window, text="แคลอรี่ที่ต้องการเพิ่ม", command=calculate_total)
total_button.pack(pady=5)



window.mainloop()