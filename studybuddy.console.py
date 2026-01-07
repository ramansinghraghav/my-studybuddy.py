import datetime
import json
import webbrowser
python_topics = ["STRINGS",
"LISTS",
"DICTIONARIES",
"TUPLES",
"SETS",
"FUNCTIONS",
"LOOPS",
"CONDITIONALS",
"OOPS",
"FILE HANDLING",
"RECURSION"
]
dsa_topics = ["ARRAYS",
    "STRINGS",
    "LINKED LISTS",
    "STACK",
    "QUEUE",
    "SORTING",
    "SEARCHING"]
    #---------function section ---------
def get_completed_topics(filename):
        try :
            with open (filename,"r") as file:
                return[line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []
def mark_topic_completed(filename, topic):
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(filename, "a") as file:
        file.write(f"{topic} - {date_time}\n")
    print(f"✅ Marked '{topic}' as completed in {filename}")

        # ---------- CORE LOGIC ----------

def get_next_topic(all_topics, completed_topics):
    for topic in all_topics:
        if topic not in completed_topics:
            return topic
    return None

def calculate_progress(all_topics, completed_topics):
    return (len(completed_topics) / len(all_topics)) * 100 if all_topics else 0

# ---------- DISPLAY FUNCTIONS ----------
def show_next_topic():
    python_done = get_completed_topics("python_completed.txt")
    dsa_done = get_completed_topics("dsa_completed.txt")
    
    py_next = get_next_topic(python_topics, python_done)
    dsa_next = get_next_topic(dsa_topics, dsa_done)
    print("\n📘 NEXT STUDY PLAN")
    print("Python:", py_next if py_next else "ALL COMPLETED")
    print("DSA   :", dsa_next if dsa_next else "ALL COMPLETED")

def show_progress():
    py_done = get_completed_topics("python_completed.txt")
    dsa_done = get_completed_topics("dsa_completed.txt")

    print("\n📊 PROGRESS")
    print(f"Python: {calculate_progress(python_topics, py_done):.2f}%")
    print(f"DSA   : {calculate_progress(dsa_topics, dsa_done):.2f}%")

def show_next_topic_link():
    try:
        with open("topics.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("❌ topics.json not found")
        return

    python_done = get_completed_topics("python_completed.txt")
    dsa_done = get_completed_topics("dsa_completed.txt")

    py_next = get_next_topic(python_topics, python_done)
    dsa_next = get_next_topic(dsa_topics, dsa_done)

    print("\n🔗 NEXT TOPIC RESOURCES")

    if py_next:
        py_link = data["python_topics"].get(py_next)
        print(f"1. Python → {py_next}: {py_link}")

    if dsa_next:
        dsa_link = data["dsa_topics"].get(dsa_next)
        print(f"2. DSA → {dsa_next}: {dsa_link}")

    choice = input("Open link? (1/2/3/0): ")

    if choice == "1" and py_next:
        webbrowser.open(data["python_topics"].get(py_next))
    elif choice == "2" and dsa_next:
        webbrowser.open(data["dsa_topics"].get(dsa_next))
    elif choice == "3":
        if py_next:
            webbrowser.open(data["python_topics"].get(py_next))
        if dsa_next:
            webbrowser.open(data["dsa_topics"].get(dsa_next))

def check_day_and_print_message():
    today = datetime.datetime.today().weekday()
    day_name = datetime.datetime.today().strftime("%A")

    print(f"\n today is {day_name}")
    
    if today == 6:
        print("Today is SUNDAY. Time to solve questions ")
    else:
        print("Today is study day:",day_name)

#---------input section ---------

def menu():
    print("""
1. Mark topic completed
2. Show next topic
3. Show progress
4. Open next topic link
0. Exit
""")

# ---------- MAIN ----------
while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        subject = input("Python or DSA: ").lower()
        topic = input("Enter topic name: ").upper()

        if subject == "python" and topic in python_topics:
            mark_topic_completed("python_completed.txt", topic)
        elif subject == "dsa" and topic in dsa_topics:
            mark_topic_completed("dsa_completed.txt", topic)
        else:
            print("❌ Invalid subject or topic")

    elif choice == "2":
        topics = "dsa_topics"
        file = "dsa_completed.txt"
        name = "DSA"
    else:
        print("❌ Invalid choice")
        continue
    completed = get_completed_topics(file)

    print(f"\n--- {name} MENU ---")
    print("1. Show Next Topic")
    print("2. Mark Topic Completed")
    print("3. Show Progress")
    print("4. Show Notes & Resources")

    action = input("Choose action: ")

    if action == "1":
            next_topic = get_next_topic(topics, completed)
            if next_topic:
                print(f"➡️ Next Topic: {next_topic}")
            else:
                print("🎉 All topics completed!")

    elif action == "2":
            topic = input("Enter topic name exactly: ").upper()
            if topic in topics and topic not in completed:
                mark_topic_completed(file, topic)
            else:
                print("❌ Invalid or already completed topic")

    elif action == "3":
            show_progress(topics, completed, name)

    elif action == "4":
            topic = input("Enter topic name: ").upper()
            show_resources(name, topic)

    else:
            print("❌ Invalid action")
check_day()

#---------output section ---------
# show_next_topic()
# show_progress()
# check_day_and_print_message()
# show_next_topic_link()