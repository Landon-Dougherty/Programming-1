import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Silver
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(36, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(696, 33)
        self._label1.TabIndex = 0
        self._label1.Text = "Speeding Ticket \"Charger\""
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(763, 451)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Prog82a"
        self.ResumeLayout(False)

