import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
        # 배경색
        self.root.configure(bg="#1e1e2e")
        
        # 변수
        self.current_operand = tk.StringVar(value="0")
        self.previous_operand = tk.StringVar(value="")
        self.operation = None
        
        # UI 구성
        self.setup_ui()
        
    def setup_ui(self):
        # 디스플레이 프레임
        display_frame = tk.Frame(self.root, bg="#2d2d3d")
        display_frame.pack(pady=20, padx=20, fill="both")
        
        # 이전 연산식 표시
        self.previous_label = tk.Label(
            display_frame,
            textvariable=self.previous_operand,
            font=("Arial", 18),
            fg="#888888",
            bg="#2d2d3d",
            anchor="e",
            height=2
        )
        self.previous_label.pack(fill="both")
        
        # 현재 입력값 표시
        self.current_label = tk.Label(
            display_frame,
            textvariable=self.current_operand,
            font=("Courier", 36, "bold"),
            fg="white",
            bg="#2d2d3d",
            anchor="e",
            height=2
        )
        self.current_label.pack(fill="both")
        
        # 버튼 프레임
        button_frame = tk.Frame(self.root, bg="#1e1e2e")
        button_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        # 버튼 레이아웃
        buttons = [
            ["AC", "DEL", "÷", "×"],
            ["7", "8", "9", "−"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "."],
            ["0", "0", "=", ""]
        ]
        
        for row_idx, row in enumerate(buttons):
            for col_idx, btn_text in enumerate(row):
                if btn_text == "":
                    continue
                    
                btn = tk.Button(
                    button_frame,
                    text=btn_text,
                    font=("Arial", 18, "bold"),
                    height=3,
                    border=0
                )
                
                # 버튼 색상 설정
                if btn_text == "AC":
                    btn.configure(bg="#ef4444", fg="white", activebackground="#dc2626")
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=4, pady=4, columnspan=1)
                elif btn_text == "DEL":
                    btn.configure(bg="#f59e0b", fg="white", activebackground="#d97706")
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=4, pady=4)
                elif btn_text == "=":
                    btn.configure(bg="#10b981", fg="white", activebackground="#059669")
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=4, pady=4, columnspan=2)
                elif btn_text in ["÷", "×", "−", "+", "."]:
                    btn.configure(bg="#667eea", fg="white", activebackground="#5568d3")
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=4, pady=4)
                elif btn_text == "0":
                    if col_idx == 0:
                        btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=4, pady=4, columnspan=2)
                    else:
                        continue
                else:
                    btn.configure(bg="#3d3d4d", fg="white", activebackground="#4d4d5d")
                    btn.grid(row=row_idx, column=col_idx, sticky="nsew", padx=4, pady=4)
                
                # 버튼 클릭 이벤트
                if btn_text == "AC":
                    btn.configure(command=self.clear)
                elif btn_text == "DEL":
                    btn.configure(command=self.delete_last)
                elif btn_text == "=":
                    btn.configure(command=self.compute)
                elif btn_text in ["÷", "×", "−", "+"]:
                    btn.configure(command=lambda op=btn_text: self.choose_operation(op))
                else:
                    btn.configure(command=lambda num=btn_text: self.append_number(num))
        
        # 그리드 행/열 비율 설정
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        
        # 키보드 이벤트
        self.root.bind("<Key>", self.on_key_press)
    
    def append_number(self, number):
        if number == "." and "." in self.current_operand.get():
            return
        
        current = self.current_operand.get()
        if current == "0" and number != ".":
            self.current_operand.set(number)
        else:
            self.current_operand.set(current + number)
    
    def clear(self):
        self.current_operand.set("0")
        self.previous_operand.set("")
        self.operation = None
    
    def delete_last(self):
        current = self.current_operand.get()
        self.current_operand.set(current[:-1] if len(current) > 1 else "0")
    
    def choose_operation(self, op):
        current = self.current_operand.get()
        if current == "":
            return
        
        if self.previous_operand.get() != "":
            self.compute()
        
        self.operation = op
        self.previous_operand.set(f"{current} {op}")
        self.current_operand.set("")
    
    def compute(self):
        if self.operation is None or self.previous_operand.get() == "":
            return
        
        try:
            prev_str = self.previous_operand.get().split()[0]
            current = self.current_operand.get()
            
            prev = float(prev_str)
            curr = float(current)
            
            if self.operation == "+":
                result = prev + curr
            elif self.operation == "−":
                result = prev - curr
            elif self.operation == "×":
                result = prev * curr
            elif self.operation == "÷":
                if curr == 0:
                    self.current_operand.set("Error")
                    return
                result = prev / curr
            
            # 정수면 정수로, 소수면 소수로 표시
            if result == int(result):
                self.current_operand.set(str(int(result)))
            else:
                self.current_operand.set(f"{result:.10g}")
            
            self.operation = None
            self.previous_operand.set("")
        
        except ValueError:
            self.current_operand.set("Error")
    
    def on_key_press(self, event):
        key = event.char
        
        if key.isdigit():
            self.append_number(key)
        elif key == ".":
            self.append_number(".")
        elif key == "+":
            self.choose_operation("+")
        elif key == "-":
            self.choose_operation("−")
        elif key == "*":
            self.choose_operation("×")
        elif key == "/":
            self.choose_operation("÷")
        elif key == "\r":  # Enter
            self.compute()
        elif key == "\x08":  # Backspace
            self.delete_last()
        
        if event.keysym == "Escape":
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
