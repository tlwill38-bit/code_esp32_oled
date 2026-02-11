import my_oled
import time
state = 0
while True:
  print(state)
  time.sleep(1)
  state = state+1
    if state > 4:
      State = 0;
    if state == 0:
      my_oled.print_text("test",0,0)
    if state == 1:
      my_oled.print_text("something else",1,0)
      
    #Line
    if state == 2:
      fill(0)
      my_oled.oled.line(0,0,10,10,1)
      oled.show()
      
    #Recatangle
    if state == 3:
      fill(0)
      my_oled.graphics.fill_rect(0,0,10,10,1)
      oled.show()

