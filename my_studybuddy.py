import datetime
from flask import Flask,render_template,request,jsonify
print("RUNNING FILE: my_studybuddy.py")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
#---------data section ---------
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
    completed = []
    try :
        with open (filename,"r") as file:
            for line in file:
                completed.append(line.strip().split(" - ")[0])
    except FileNotFoundError:
        pass
    return completed

def is_topic_completed(filename, topic):
    completed = get_completed_topics(filename)
    return topic in completed

def mark_topic_completed(filename, topic):
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open(filename, "a") as file:
        file.write(f"{topic} - {date_time}\n")

        # ---------- CORE LOGIC ----------

def get_next_topic(all_topics, completed_topics):
    for topic in all_topics:
        if topic not in completed_topics:
            return topic
    return None

def calculate_progress(all_topics, completed_topics):
    if not all_topics:
        return 0
    return round((len(completed_topics) / len(all_topics)) * 100,2)
#---------input section ---------

@app.route("/next-topic")
def next_topic():
    return jsonify({
        "python": get_next_topic(
            python_topics,
            get_completed_topics("python_completed.txt")
        ),
        "dsa": get_next_topic(
            dsa_topics,
            get_completed_topics("dsa_completed.txt")
        )
    })

@app.route("/mark-completed", methods=["POST"])
def mark_completed():
    data = request.json

    if not data or "subject" not in data or "topic" not in data:
        return jsonify({"error": "Invalid data"}), 400

    subject = data["subject"]
    topic = data["topic"].strip().upper()

    if subject == "python":
        if is_topic_completed("python_completed.txt", topic):
            return jsonify({
            "status": "duplicate", 
        "message": "Topic already completed"
        })
        mark_topic_completed("python_completed.txt", topic)
    
    elif subject == "dsa":
        if is_topic_completed("dsa_completed.txt", topic):
           return jsonify({
               "status": "duplicate",
                "message": "Topic already completed"
             })
        mark_topic_completed("dsa_completed.txt", topic)
    else:   
        return jsonify({"error": "Invalid subject"}), 400

    return jsonify({"status": "success"})


@app.route("/progress")
def progress():
    return jsonify({
        "python": calculate_progress(
            python_topics,
            get_completed_topics("python_completed.txt")
        ),
        "dsa": calculate_progress(
            dsa_topics,
            get_completed_topics("dsa_completed.txt")
        )
    })

@app.route("/test-date")
def test_date():
    return jsonify({
        "topic": "STRINGS",
        "date": "2026-01-07 14:30"
    })

@app.route("/reset", methods=["POST"])

def reset_progress():
    open("python_completed.txt", "w").close()
    open("dsa_completed.txt", "w").close()
    return jsonify({"status": "reset-success"})

@app.route("/all-topics")
def all_topics():
    python_done = get_completed_topics("python_completed.txt")
    dsa_done = get_completed_topics("dsa_completed.txt")

    return jsonify({
        "python": [
            {"name": topic, "completed": topic in python_done}
            for topic in python_topics
        ],
        "dsa": [
            {"name": topic, "completed": topic in dsa_done}
            for topic in dsa_topics
        ]
    })

@app.route("/test-mark")
def test_mark():
    return jsonify({"msg": "Server is working"})

@app.route("/completed-with-date")
def completed_with_date():
    result = []

    try:
        with open("python_completed.txt", "r") as file:
            for line in file:
                topic, datetime_str = line.strip().split(" - ")
                date = datetime_str.split(" ")[0]
                result.append({
                    "topic": topic,
                    "date": date
                })
    except FileNotFoundError:
        pass

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)




