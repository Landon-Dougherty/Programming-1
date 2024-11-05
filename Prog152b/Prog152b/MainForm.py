import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 498)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(192, 98)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(274, 498)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(192, 98)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(535, 498)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(192, 98)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(715, 429)
        self._listBox1.TabIndex = 3
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(50, 447)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 20)
        self._textBox1.TabIndex = 4
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(50, 472)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 5
        self._label1.Text = "Enter Common Int."
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self.ClientSize = System.Drawing.Size(766, 618)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Prog152a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        total = 0 
        input = int(self._textBox1.Text)
        for num in range (2,input+1,2):
            total += num
            rest = str(num) + "\t\t" + str(total)
            self._listBox1.Items.Add(rest)

    def Button2Click(self, sender, e):#Clear
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):#Exit
        Application.Exit()
        
        