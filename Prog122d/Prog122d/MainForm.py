import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 20
        self._listBox1.Location = System.Drawing.Point(9, 18)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(735, 504)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(9, 543)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(197, 79)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(287, 543)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(197, 79)
        self._button2.TabIndex = 2
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(547, 543)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(197, 79)
        self._button3.TabIndex = 3
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self.ClientSize = System.Drawing.Size(763, 634)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Prog122d"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        Header = "Numbers\t\t\t\t\tEquation"
        self._listBox1.Items.Add(Header)
        for num in range (-12,16+1):
            first = num**6
            second = 3*(num)**5
            third = 93*(num)**4
            fourth = 87*(num)**3
            fifth = 1596*(num)**2
            sixth = 1380*(num)
            seventh = 2800
            total = first - second - third + fourth + fifth - sixth - seventh
            list = str(num) + "\t\t\t\t\t" + str(total)
            self._listBox1.Items.Add(list)
            

    def Button2Click(self, sender, e):
        Application.Exit()
        

    def Button3Click(self, sender, e):
        self._listBox1.Items.Clear()