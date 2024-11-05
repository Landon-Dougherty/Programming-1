import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(42, 50)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(309, 34)
        self._textBox1.TabIndex = 0
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 17.5, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(42, 253)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(309, 34)
        self._textBox2.TabIndex = 1
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label1.Location = System.Drawing.Point(42, 146)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(308, 38)
        self._label1.TabIndex = 2
        self._label1.Text = "Operation :"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(537, 50)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(75, 60)
        self._button1.TabIndex = 3
        self._button1.Text = "+"
        self._button1.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self.ClientSize = System.Drawing.Size(871, 624)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Name = "MainForm"
        self.Text = "Prog140"
        self.ResumeLayout(False)
        self.PerformLayout()

