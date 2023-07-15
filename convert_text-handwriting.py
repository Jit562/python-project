import pywhatkit as pw

world = ["Python is an interpreted", "object-oriented", "high-level programming language with dynamic semantics", "Its high-level built in data structures", "combined with dynamic typing and dynamic"]

pw.text_to_handwriting(world, "demo.png", [0,0,138])
print("End")