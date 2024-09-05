import subprocess
import sys
import json
import re
import tkinter as tk
from tkinter import ttk


args = sys.argv
hikisuu = "a"
language = 'node'

if len(args) >= 2:
  if args[1] == 'node':
    print('test')
  else:
    hikisuu = args[1]

def test():
  hikisuu = az_Entry.get()
  value = radio_value.get()
  
  print(f'hikisuu: {hikisuu}, radio_value: {radio_value}, valuve: {value}')
  
  run(con_namber=value, data=hikisuu)

def json_read(filename):
  with open(filename, mode='r', encoding="utf-8") as f :
    data = json.load(f)
  print(f'{filename}を読み込みました')
  return data

def json_write(filename, data):
  with open (filename, mode="w", encoding="utf-8") as w:
    json.dump(data, w, indent=2)
  print(f'{filename}へ書き込ました')
  return

def text_write(filename, text):
  with open (file=filename, mode='w+',encoding='utf-8') as w:
    w.write(str(text))
  print(f'{filename}へ書き込ました')

def run(con_namber, data):
  converter_data = [
    "./converter/F``k.js",
    "./converter/convert.py",
    "./converter/convert.js",
    "convert_elements.py"
    ]
  if con_namber == 1 or con_namber == 3:
    language = 'python3'
  else:
    language = 'node'
  converter = converter_data[con_namber]
  print(f'{converter} を実行')
  result = subprocess.run([language, converter, data], bufsize=0, stdout=subprocess.PIPE)
  result_str = str(result.stdout)
  result_list = re.split('\\\\n',result_str)
  print(f'data: {result_list}, \ndata[1]: {result_list[1]} \ntype: {type(result_list)}')
  az_Entry.delete(0,tk.END)
  return_Textarea.delete(1.0,tk.END)
  return_Textarea.insert(tk.END, result_list[1])



root = tk.Tk()
root.title(u"converter")
root.geometry("500x1000")

frame0 = tk.Frame(root)
#frame0.pack()

converter_frame = tk.LabelFrame(
  root,
  font=("MSゴシック","20","normal"),
  labelanchor="n",
  text='converter',
  width=200,
  height=300,
  padx=22,
  pady=5
  )
return_frame = tk.LabelFrame(
  root,
  font=("MSゴシック","20","normal"),
  labelanchor="n",
  text='出力',
  width=400,
  height=300,
  )
radio_value = tk.IntVar()



radio_jsfuck = tk.Radiobutton(
  converter_frame,
  font=("MSゴシック","24","normal"),
  text='JSFuck',
  value=0,
  variable=radio_value,
)

radio_python = tk.Radiobutton(
  converter_frame,
  font=("MSゴシック","25","normal"),
  text='Python',
  value=1,
  variable=radio_value
)
radio_js = tk.Radiobutton(
  converter_frame,
  font=("MSゴシック","26","normal"),
  text='js',
  value=2,
  variable=radio_value
)
radio_jsfuck_jsfuck = tk.Radiobutton(
  converter_frame,
  font=("MSゴシック","16","normal"),
  text='jsfuckをjsfuckにするやつ',
  value=3,
  variable=radio_value
)

az_Entry = tk.Entry(
  root,
  width=17,
)
az_Entry.insert(0,"f")

start_button = tk.Button(
  root,
  text='実行',
  command=test,
  width=15,
  height=1
)


return_Textarea = tk.Text(
  return_frame,
  width=400,
  height=23
)
return_Textarea.insert(tk.END,"(+([+!![]]+[!![]+!![]+!![]+!![]+!![]]))[(!![]+[])[+[]]+([][[((![]+[])[+!![]])+((!![]+[])[+[]])]]+[])[+!![]+!![]+!![]+!![]+!![]+!![]]+(+[!![]]+([]+[])[([][[((![]+[])[+!![]])+((!![]+[])[+[]])]]+[])[+!![]+!![]+!![]]+([][[((![]+[])[+!![]])+((!![]+[])[+[]])]]+[])[+!![]+!![]+!![]+!![]+!![]+!![]]+(([][[]])+[])[+!![]]+(![]+[])[+!![]+!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[+!![]]+(([]+[[]])[+[]]+[])[+[]]+([][[((![]+[])[+!![]])+((!![]+[])[+[]])]]+[])[+!![]+!![]+!![]]+(!![]+[])[+[]]+([][[((![]+[])[+!![]])+((!![]+[])[+[]])]]+[])[+!![]+!![]+!![]+!![]+!![]+!![]]+(!![]+[])[+!![]]]+[])[(+!![])+(+!![]+!![]+[])]+(!![]+[])[+[]]+(!![]+[])[+!![]]+(([]+[[]])[+[]]+[])[+!![]+!![]+!![]+!![]+!![]]+(([][[]])+[])[+!![]]+(([]+[])[([][[((![]+[])[+!![]])+((!![]+[])[+[]])]]+[])[+!![]+!![]+!![]]+([][[((![]+[])[+!![]])+((!![]+[])[+[]])]]+[])[+!![]+!![]+!![]+!![]+!![]+!![]]+(([][[]])+[])[+!![]]+(![]+[])[+!![]+!![]+!![]]+(!![]+[])[+[]]+(!![]+[])[+!![]]+(([]+[[]])[+[]]+[])[+[]]+([][[((![]+[])[+!![]])+((!![]+[])[+[]])]]+[])[+!![]+!![]+!![]]+(!![]+[])[+[]]+([][[((![]+[])[+!![]])+((!![]+[])[+[]])]]+[])[+!![]+!![]+!![]+!![]+!![]+!![]]+(!![]+[])[+!![]]]+[])[+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]+!![]]]((+!![]+!![]+!![])+(+!![]+!![]+!![]+!![]+!![]+!![]+[]))")

converter_frame.pack()
radio_jsfuck.pack()
radio_python.pack()
radio_js.pack()
radio_jsfuck_jsfuck.pack()
az_Entry.pack()
start_button.pack()
return_frame.pack()
return_Textarea.pack()


root.mainloop()