import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(36, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(696, 33)
        self._label1.TabIndex = 0
        self._label1.Text = "Speeding Ticket \"Charger\""
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(319, 62)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(131, 45)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(319, 135)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(131, 45)
        self._textBox2.TabIndex = 2
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 62)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(289, 45)
        self._label2.TabIndex = 3
        self._label2.Text = "Enter Speed Limit ---->"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(462, 62)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(289, 45)
        self._label3.TabIndex = 4
        self._label3.Text = "<---- Enter Speed Limit "
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(462, 135)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(289, 45)
        self._label4.TabIndex = 5
        self._label4.Text = "<---- Enter Speed Recorded"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(12, 135)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(289, 45)
        self._label5.TabIndex = 6
        self._label5.Text = "Enter Speed Recorded ---->"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(236, 183)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(289, 156)
        self._label6.TabIndex = 7
        self._label6.Text = """Ticket 
--  |  --
--  |  --
  --  |  -- 
  \\/ """
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0, True)
        self._label7.ForeColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label7.Location = System.Drawing.Point(222, 328)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(321, 88)
        self._label7.TabIndex = 8
        self._label7.Text = "Ticket = "
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 209)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(289, 103)
        self._button1.TabIndex = 9
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(462, 209)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(289, 103)
        self._button2.TabIndex = 10
        self._button2.Text = "Calculate"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button1Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(12, 322)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(192, 103)
        self._button3.TabIndex = 11
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        # 
        # button4
        # 
        self._button4.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(559, 322)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(192, 103)
        self._button4.TabIndex = 12
        self._button4.Text = "Clear "
        self._button4.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
        self.ClientSize = System.Drawing.Size(763, 451)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog82a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        SpeedLimit = float(self._textBox1.Text)
        Speed      = float(self._textBox2.Text) 
        SpeedOverLimit = int(Speed - SpeedLimit)
        PricePerMile = int(SpeedOverLimit * 5.00)
        Ticket = 20.00
        TotalTicket = int(PricePerMile + Ticket)
        self._label7.Text = "Ticket = " + str(TotalTicket)
        