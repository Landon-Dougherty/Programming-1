import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._panel1 = System.Windows.Forms.Panel()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._panel1.SuspendLayout()
        self.SuspendLayout()
        # 
        # radioButton1
        # 
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(17, 24)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(144, 48)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Channel 1 "
        self._radioButton1.UseVisualStyleBackColor = True
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # panel1
        # 
        self._panel1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._panel1.Controls.Add(self._checkBox3)
        self._panel1.Controls.Add(self._checkBox2)
        self._panel1.Controls.Add(self._checkBox1)
        self._panel1.Controls.Add(self._radioButton3)
        self._panel1.Controls.Add(self._radioButton2)
        self._panel1.Controls.Add(self._radioButton1)
        self._panel1.Location = System.Drawing.Point(51, 35)
        self._panel1.Name = "panel1"
        self._panel1.Size = System.Drawing.Size(462, 243)
        self._panel1.TabIndex = 1
        # 
        # radioButton2
        # 
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(17, 89)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(144, 48)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Channel 2"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(17, 164)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(144, 48)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Channel 3"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # checkBox1
        # 
        self._checkBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox1.Location = System.Drawing.Point(279, 32)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(104, 40)
        self._checkBox1.TabIndex = 3
        self._checkBox1.Text = "Channel 4"
        self._checkBox1.UseVisualStyleBackColor = True
        # 
        # checkBox2
        # 
        self._checkBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox2.Location = System.Drawing.Point(279, 97)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(104, 40)
        self._checkBox2.TabIndex = 4
        self._checkBox2.Text = "Channel 5"
        self._checkBox2.UseVisualStyleBackColor = True
        # 
        # checkBox3
        # 
        self._checkBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._checkBox3.Location = System.Drawing.Point(279, 169)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(104, 40)
        self._checkBox3.TabIndex = 5
        self._checkBox3.Text = "Channel 6"
        self._checkBox3.UseVisualStyleBackColor = True
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(90, 334)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(147, 43)
        self._button1.TabIndex = 2
        self._button1.Text = "Okay"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(330, 334)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(147, 43)
        self._button2.TabIndex = 3
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self.ClientSize = System.Drawing.Size(583, 466)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._panel1)
        self.Name = "MainForm"
        self.Text = "Prog247"
        self.Load += self.MainFormLoad
        self._panel1.ResumeLayout(False)
        self.ResumeLayout(False)


    def RadioButton1CheckedChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        first = 0
        if radioButton1.Checked:
            first = "Channel 1"
        elif radioButton2.Checked:
            first = "Channel 2"
        elif radioButton3.Checked:
            first = "Channel 3"
        else:
            return

        