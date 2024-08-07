import tkinter as tk
import random

class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kiểm Tra Toán Phép Cộng Trừ")
        self.root.geometry("600x600")
        self.root.configure(bg="#e0f7fa")
        
        self.questions = []
        self.create_questions()
        
        self.current_question = 0
        self.score = 0
        self.time_left = 600  

        self.create_widgets()
        self.update_timer()

    def create_questions(self):
        for _ in range(10):
            num1 = random.randint(100000, 999999)
            num2 = random.randint(100000, 999999)
            if (num1 < num2):
                t = num1
                num1 = num2
                num2 = t
            if random.choice([True, False]):
                question = f"{num1} + {num2} = ?"
                answer = num1 + num2
            else:
                question = f"{num1} - {num2} = ?"
                answer = num1 - num2
            self.questions.append((question, answer))

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Kiểm Tra Toán Phép Cộng Trừ", font=('Times New Roman', 24, 'bold'), bg="#e0f7fa", fg="#00695c")
        self.title_label.pack(pady=20)

        self.frame = tk.Frame(self.root, bg="#ffffff", bd=2, relief=tk.RIDGE)
        self.frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.question_label = tk.Label(self.frame, text=self.questions[self.current_question][0], font=('Times New Roman', 18), bg="#ffffff", fg="#004d40")
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.frame, font=('Times New Roman', 18), width=10, bd=2, relief=tk.RIDGE)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.frame, text="Nộp Bài", command=self.check_answer, font=('Times New Roman', 16, 'bold'), bg="#00796b", fg="#ffffff", bd=2, relief=tk.RIDGE)
        self.submit_button.pack(pady=20)

        self.result_label = tk.Label(self.frame, text="", font=('Times New Roman', 18), bg="#ffffff", fg="#004d40")
        self.result_label.pack(pady=20)

        self.timer_label = tk.Label(self.root, text=f"Thời gian còn lại: {self.time_left} giây", font=('Times New Roman', 24, 'bold'), bg="#e0f7fa", fg="#d32f2f")
        self.timer_label.pack(pady=20)

        self.capybara_canvas = tk.Canvas(self.root, width=200, height=200, bg="#e0f7fa", highlightthickness=0)
        self.capybara_canvas.pack(pady=20)
        self.draw_capybara()

    def draw_capybara(self):
        # Body
        self.capybara_canvas.create_oval(50, 70, 150, 130, fill="#a67c52", outline="#a67c52")
        # Head
        self.capybara_canvas.create_oval(60, 40, 110, 80, fill="#a67c52", outline="#a67c52")
        # Eyes
        self.capybara_canvas.create_oval(75, 55, 80, 60, fill="#000000")
        self.capybara_canvas.create_oval(90, 55, 95, 60, fill="#000000")
        # Nose
        self.capybara_canvas.create_oval(85, 70, 90, 75, fill="#000000")
        # Ears
        self.capybara_canvas.create_oval(55, 35, 65, 45, fill="#a67c52", outline="#a67c52")
        self.capybara_canvas.create_oval(105, 35, 115, 45, fill="#a67c52", outline="#a67c52")
        # Legs
        self.capybara_canvas.create_oval(60, 120, 70, 130, fill="#a67c52", outline="#a67c52")
        self.capybara_canvas.create_oval(130, 120, 140, 130, fill="#a67c52", outline="#a67c52")

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Thời gian còn lại: {self.time_left} giây")
            self.root.after(1000, self.update_timer)
        else:
            self.end_quiz()

    def check_answer(self):
        user_answer = self.answer_entry.get()
        try:
            user_answer = int(user_answer)
            correct_answer = self.questions[self.current_question][1]
            if user_answer == correct_answer:
                self.score += 1
                self.result_label.config(text="Đúng!", fg="green")
            else:
                self.result_label.config(text=f"Sai! Đáp án đúng là {correct_answer}", fg="red")
        except ValueError:
            self.result_label.config(text="Vui lòng nhập một số hợp lệ!", fg="red")
            return

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question][0])
            self.answer_entry.delete(0, tk.END)
        else:
            self.end_quiz()

    def end_quiz(self):
        self.question_label.pack_forget()
        self.answer_entry.pack_forget()
        self.submit_button.pack_forget()
        self.result_label.config(text=f"Hoàn thành! Bạn đã trả lời đúng {self.score} trên 10 câu hỏi.", fg="#333")
        self.timer_label.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = MathQuizApp(root)
    root.mainloop()
''' write by khanhduy 7/8/24'''
