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
        self._listBox1.Font = System.Drawing.Font("Microsoft Tai Le", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 25
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(743, 279)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(16, 340)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(185, 258)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(286, 340)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(185, 258)
        self._button2.TabIndex = 2
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(546, 340)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(185, 258)
        self._button3.TabIndex = 3
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self.ClientSize = System.Drawing.Size(767, 626)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Prog122c"
        self.ResumeLayout(False)


    def Button2Click(self, sender, e):
        Application.Exit()

    def Button3Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button1Click(self, sender, e):
        for column1 in range (0,11,2):
            column2 = column1 + 1
            column3 = column1 * 2
            column4 = column1 * 10 
            first = str(column1) + "\t" + str(column2) + "\t" + str(column3) + "\t" + str(column4)
            self._listBox1.Items.Add(first)
         
            
        
        '''First = [2,3,4,4] 
        self._listBox1.Items.Add(str(First))
        Second = [(First[0])*2]
        self._listBox1.Items.Add(str(Second))'''
        
     
