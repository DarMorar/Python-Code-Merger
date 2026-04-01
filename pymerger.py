import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import subprocess
import platform

class MergeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Объединение файлов *.py в TXT")
        self.root.geometry("600x500")
        self.root.resizable(True, True)

        self.selected_files = []
        self.output_path = ""

        self.create_widgets()

    def create_widgets(self):
        frame_files = tk.LabelFrame(self.root, text="1. Выберите файлы *.py", padx=5, pady=5)
        frame_files.pack(fill="both", expand=True, padx=10, pady=5)

        btn_select_files = tk.Button(frame_files, text="Добавить файлы", command=self.select_files)
        btn_select_files.pack(anchor="w", pady=5)

        self.listbox_files = tk.Listbox(frame_files, selectmode=tk.EXTENDED, height=8)
        self.listbox_files.pack(fill="both", expand=True, pady=5)

        btn_remove_selected = tk.Button(frame_files, text="Удалить выбранные", command=self.remove_selected)
        btn_remove_selected.pack(side="left", padx=5)

        btn_clear_all = tk.Button(frame_files, text="Очистить весь список", command=self.clear_all)
        btn_clear_all.pack(side="left", padx=5)

        frame_output = tk.LabelFrame(self.root, text="2. Укажите файл для сохранения", padx=5, pady=5)
        frame_output.pack(fill="x", padx=10, pady=5)

        self.output_entry = tk.Entry(frame_output, textvariable=tk.StringVar(), state="readonly")
        self.output_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

        btn_browse_output = tk.Button(frame_output, text="Обзор...", command=self.select_output)
        btn_browse_output.pack(side="right")

        self.open_folder_var = tk.BooleanVar(value=True)
        chk_open_folder = tk.Checkbutton(
            self.root,
            text="После создания файла открыть папку с выделением файла",
            variable=self.open_folder_var
        )
        chk_open_folder.pack(pady=(5, 0))

        btn_merge = tk.Button(self.root, text="3. Объединить файлы", command=self.merge_files,
                              bg="lightgreen", font=("Arial", 10, "bold"))
        btn_merge.pack(pady=10)

        self.status_label = tk.Label(self.root, text="Готов к работе", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)

    def select_files(self):
        files = filedialog.askopenfilenames(
            title="Выберите Python-файлы",
            filetypes=[("Python files", "*.py"), ("All files", "*.*")]
        )
        for f in files:
            if f not in self.selected_files:
                self.selected_files.append(f)
                self.listbox_files.insert(tk.END, f)
        self.update_status(f"Добавлено файлов: {len(files)}")

    def remove_selected(self):
        selected_indices = self.listbox_files.curselection()
        for idx in reversed(selected_indices):
            del self.selected_files[idx]
            self.listbox_files.delete(idx)
        self.update_status("Выбранные файлы удалены")

    def clear_all(self):
        self.selected_files.clear()
        self.listbox_files.delete(0, tk.END)
        self.update_status("Список файлов очищен")

    def select_output(self):
        file_path = filedialog.asksaveasfilename(
            title="Сохранить результат как",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.output_path = file_path
            self.output_entry.config(state="normal")
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, file_path)
            self.output_entry.config(state="readonly")
            self.update_status(f"Файл сохранения: {os.path.basename(file_path)}")

    def open_file_location(self, file_path):
        """Открывает папку и выделяет указанный файл (Windows) или просто папку (macOS/Linux)"""
        folder_path = os.path.dirname(file_path)
        
        if not os.path.exists(folder_path):
            return False
        
        try:
            system = platform.system()
            
            if system == "Windows":
                # Нормализуем путь (обратные слеши, абсолютный)
                file_path = os.path.normpath(os.path.abspath(file_path))
                
                # Используем PowerShell для надёжного выделения файла
                ps_command = f'Start-Process explorer "/select, `"{file_path}`""'
                subprocess.run(['powershell', '-Command', ps_command], check=True, shell=False)
                return True
                
            elif system == "Darwin":  # macOS
                subprocess.run(['open', '-R', file_path], check=True)
                return True
                
            elif system == "Linux":
                subprocess.run(['xdg-open', folder_path], check=True)
                return True
            else:
                return False
                
        except Exception as e:
            print(f"Не удалось выделить файл: {e}")
            # Запасной вариант: просто открыть папку
            try:
                if system == "Windows":
                    subprocess.run(['explorer', folder_path], check=True)
                return True
            except:
                return False

    def merge_files(self):
        if not self.selected_files:
            messagebox.showwarning("Нет файлов", "Сначала выберите хотя бы один файл *.py.")
            return
        if not self.output_path:
            messagebox.showwarning("Нет места сохранения", "Укажите, куда сохранить итоговый TXT-файл.")
            return

        try:
            with open(self.output_path, 'w', encoding='utf-8') as outfile:
                outfile.write(f"# Объединённый файл создан: {self.get_current_time()}\n")
                outfile.write(f"# Всего объединено файлов: {len(self.selected_files)}\n\n")
                
                for filepath in self.selected_files:
                    filename = os.path.basename(filepath)
                    outfile.write(f"=== {filename} ===\n")
                    try:
                        with open(filepath, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            outfile.write(content)
                            if not content.endswith('\n'):
                                outfile.write('\n')
                    except Exception as e:
                        outfile.write(f"Ошибка при чтении файла {filename}: {str(e)}\n")
                    outfile.write("\n")
            
            self.update_status(f"Готово! Файл сохранён: {self.output_path}")
            
            if self.open_folder_var.get():
                result = messagebox.askyesno(
                    "Успех",
                    f"Объединение завершено!\n\n"
                    f"Файл сохранён:\n{self.output_path}\n\n"
                    f"Всего объединено файлов: {len(self.selected_files)}\n\n"
                    f"Открыть папку с выделением этого файла?"
                )
                if result:
                    self.open_file_location(self.output_path)
            else:
                messagebox.showinfo(
                    "Успех",
                    f"Объединение завершено!\n\n"
                    f"Файл сохранён:\n{self.output_path}\n\n"
                    f"Всего объединено файлов: {len(self.selected_files)}"
                )
            
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось записать итоговый файл:\n{str(e)}")
            self.update_status("Ошибка при записи")

    def get_current_time(self):
        from datetime import datetime
        return datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    def update_status(self, message):
        self.status_label.config(text=message)
        self.root.update_idletasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = MergeApp(root)
    root.mainloop()