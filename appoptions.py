def startAppOption():
  def instApp(): 
      clr()
      def inst():
          try:
              out = sp.check_output("zaglarh install " + "\"" + apkF + "\"")
              apkN = apkF.rpartition (".")
              mb.showinfo ("Success", "Successfully installed " + apkN[0])
          except:
              mb.showerror ("Error", "TeLon encountered a problem!!!")
      apkF = fd.askopenfilename (title = "Choose an APK file")
      if apkF == "":
          mb.showerror ("Error", "Choose a file.")
      else:
          apkF_P = apkF.rpartition (".")
          if apkF_P[2] != "apk":
              mb.showerror ("Error", "Invalid file type.")
              instApp()
          else:
              inst()

  def instAppUp():
      clr()
      mb.showinfo ("App Update Installation", "Is the APP(s) in TeLonLogs/Apk Folder.\nPress OK to confirm.")
      try:
          appPath = gd.path.join("C:\\","TeLonLogs\\","APK_to_inst\\")
          lDir = gd.listdir(appPath)
          dirL = len (lDir) #get the length of the list but its an integer
          sDirL = str(dirL)#convert the int to str in order to concatenate in the future.
          for i in lDir:
              initialO = sp.check_output("zaglarh install " + appPath + i)
              up1 = str(initialO).rpartition("Install\\r\\n")
              up2 = up1[2].rpartition("\\r\\n")
              state = up2[0]
              #print (state)
              clr()
              if state == "Success":mb.showinfo("Success", i + " has been installed.")
          mb.showinfo("Success", sDirL + " Apps has been installed.")

      except sp.CalledProcessError: #Error to display if more tha 1 devices are connected or if the device has been connected.
          clr()
          mb.showerror("Error", "TeLon encountered an error!!!.")

  def unInst(): # add option for user to back-out or proceed
      def un():
          try:
              dumpedA = unName.get()
              un1 = gd.system("zaglarh shell pm list packages | findstr " + dumpedA) #god returns 0 if a package was found during the search but returns 1 if not
              #clr()
              if un1 == 0:
                  un2 = sp.check_output("zaglarh shell pm list packages | grep " + dumpedA)
                  un3 = str(un2).rpartition(":")
                  un4 = un3 [2]
                  un5 = un4.rpartition ("\\r")
                  un6 = un5 [0]
                  res = mb.askquestion ("Warning", "Proceed to uninstall " + un6)
                  if res == "yes":
                      sp.check_output("zaglarh uninstall " + un6)
                      clr()
                      mb.showinfo ("Success", "TeLon has successfully removed " + un6)
              else:
                  mb.showerror ("Error", "App not found!!!")
          except sp.CalledProcessError:
              clr()
              mb.showerror("Error", "TeLon encountered a problem!!!")

      clr()
      unInstWin = Tk()
      unInstWin.title ("Uninstall App")
      unInstWin.geometry("280x130+540+310")
      unName = StringVar()
      uLab = Label (unInstWin, text = "App Name", font = ("times new roman", 12, "bold")).place (x=0,y=20,relwidth=1)
      uEntry = Entry (unInstWin, width =30, textvariable = unName, bg = "WHITE", bd = 5).place (x=45, y = 60)
      uconfB = Button (unInstWin, command = un, text = "Uninstall", bg = "Red", fg = "WHITE").place (x=115, y=95)
      unInstWin.mainloop()

  def instApps():
      clr()
      try:
          """appPath = gd.path.join("C:\\","TeLonLogs\\","APK_to_inst\\")#TODO check if they are apk files
          lDir = gd.listdir(appPath)
          dirL = len (lDir) #get the length of the list but its an integer
          sDirL = str(dirL)#convert the int to str in order to concatenate in the future."""
          apkL = fd.askopenfilenames (title = "Choose APk file(s)")
          for apkF in apkL:
              fType = apkF.rpartition(".")
              ft =fType[2]
              if ft == "apk":
                  #mb.showinfo ("Success", "This is an APK file" + apkF)
                  initialO = sp.check_output("zaglarh install " + "\"" + apkF + "\"")
                  p1 = str(initialO).rpartition("Install\\r\\n")
                  p2 = p1[2].rpartition("\\r\\n")
                  state = p2[0]
                  #print (state)
                  clr()
                  #if state == "Success":mb.showinfo("Success", apkF + " has been installed.")
              else:
                  mb.showerror ("Error", "This is not a valid APK file. " + apkF)
                  gd.system ("exit")
          mb.showinfo("Success", str(len(apkL)) + " Apps have been installed.")
      except sp.CalledProcessError: #Error to display if more tha 1 devices are connected or if the device has been connected.
          #clr()
          mb.showerror("Error", "TeLon encountered a error!!!. App(s) could not be installed.")

  def lnchA():
      def lnch():
          try:
              dumpedLA = lnchName.get()
              lnch1 = sp.check_output("zaglarh shell pm list packages | findstr " + dumpedLA) #gd returns 0 if a package was found during the search but returns 1 if not
              #clr()
              if lnch1 == 0:
                  lnch2 = sp.check_output("zaglarh shell pm list packages | grep " + dumpedLA)
                  lnch3 = str(lnch2).rpartition(":")
                  lnch4 = lnch3 [2]
                  lnch5 = lnch4.rpartition ("\\r")
                  lnch6 = lnch5 [0]
                  sp.check_output("zaglarh shell monkey -p " + lnch6 + " 1")
                  clr()
                  mb.showinfo ("Success", "TeLon has successfully launched " + lnch6)
              else:mb.showerror ("Error", "App not found!!!")
          except sp.CalledProcessError:
              clr()
              mb.showerror("Error", "TeLon encountered a problem!!!")
      clr()
      lnchWin = Tk()
      lnchWin.title ("Launch an App")
      lnchWin.geometry("280x130+540+310")
      lnchName = StringVar()
      lLab = Label (lnchWin, text = "App Name", font = ("times new roman", 12, "bold")).place (x=0,y=20,relwidth=1)
      lEntry = Entry (lnchWin, width =30, textvariable = lnchName, bg = "WHITE", bd = 5).place (x=45, y = 60)
      lconfB = Button (lnchWin, command = lnch, text = "Launch", bg = "Red", fg = "WHITE").place (x=115, y=95)
      lnchWin.mainloop()

  def puApp():
      def pu():
          try:
              gd.chdir (telonLog)
              dumpedPu = puName.get()
              pu1 = gd.system("zaglarh shell pm list packages | findstr " + dumpedPu) #god returns 0 if a package was found during the search but returns 1 if not
              clr()
              if pu1 == 0:
                  pu2 = sp.check_output("zaglarh shell pm list packages | grep " + dumpedPu)
                  pu3 = str(pu2).rpartition(":")
                  pu4 = pu3 [2]
                  pu5 = pu4.rpartition ("\\r")
                  pu6 = pu5 [0]
                  pthOut = sp.check_output("zaglarh shell pm path " + pu6)
                  pu7 = str(pthOut).rpartition(":")
                  pu8 = pu7 [2]
                  pu9 = pu8.rpartition("\\r")
                  puA = pu9 [0]
                  gd.system("zaglarh pull " + puA + " " + telonLog)
                  gd.system("rename " + telonLog + "base.apk " + pu6 + ".apk")
                  clr()
                  gd.system ("start.")
                  mb.showinfo ("Success", "TeLon has successfully pulled apk file of " + pu6)
              else:mb.showerror ("Error", "App not found!!!")
          except sp.CalledProcessError:
              clr()
              mb.showerror("Error", "TeLon encountered a problem!!!")

      clr()
      puWin = Tk()
      puWin.title ("Pull Apk File")
      puWin.geometry("280x130+540+310")
      puName = StringVar()
      pLab = Label (puWin, text = "App Name", font = ("times new roman", 12, "bold")).place (x=0,y=20,relwidth=1)
      pEntry = Entry (puWin, width =30, textvariable = puName, bg = "WHITE", bd = 5).place (x=45, y = 60)
      pconfB = Button (puWin, command = pu, text = "Pull", bg = "Red", fg = "WHITE").place (x=115, y=95)
      puWin.mainloop()
startAppOption()
