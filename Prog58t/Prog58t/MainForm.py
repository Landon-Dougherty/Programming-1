import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label3 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 256)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(561, 193)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 186)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(561, 50)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate Change"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(24, 21)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(246, 38)
        self._textBox1.TabIndex = 3
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(24, 71)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(246, 45)
        self._label2.TabIndex = 5
        self._label2.Text = "Total Due"
        self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(47, 135)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(204, 45)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear Data"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(350, 135)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(204, 45)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(327, 71)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(246, 45)
        self._label3.TabIndex = 8
        self._label3.Text = "Total Paid"
        self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(327, 21)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(246, 38)
        self._textBox2.TabIndex = 9
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Black
        self.ClientSize = System.Drawing.Size(602, 458)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog58t"
        self.ResumeLayout(False)
        self.PerformLayout()

    def Button1Click(self, sender, e):
        Total  = float(self._textBox1.Text)
        Paid   = float(self._textBox2.Text)
        Change = float(Paid - Total)
        QuarterChange = 0
        ChangeAfterQuarters = 
        DimeChange = 
        
        if QuarterChange ==4:
            DimeChange = 0 
        
        if int(Change / 0.25) < 0:
            QuarterChange = int((Change / 0.25) * -1)
        else:
            QuarterChange = int(Change / 0.25)                                    
        
        self._label1.Text = "Total = " + str(Total) + "\nPaid = " + str(Paid) + "\nChange = " + str(Total - Paid) +\
        "\nQuartersDue = " + str(QuarterChange) + "\nDimes Due = " + str(DimeChange)
        
    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._label1.Text   = ""
        