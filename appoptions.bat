::::create funtion for options related to apps
:jayhackappoption
  cls
  echo ++++++++++++++++++++++++++
  echo Hi  %username%, welcome..
  echo ++++++++++++++++++++++++++
  Title App control page
  echo.
  echo Put in the options below or "b" to go back.
  echo 1) Launch an app
  echo 2) Install an App
  echo 3) Install an App update
  echo 4) Uninstall an App
  echo 5) Pull the raw apk file of any App
  echo.
  echo ++++++++++
  set /p appcontrol=Put it in: 
  if "%appcontrol%"=="b" (
    goto jayhackpage
    )
  if "%appcontrol%"=="1" (
    goto jayhacklaunchapp
    )
  if "%appcontrol%"=="2" (
    goto jayhackinstall
    )
  if "%appcontrol%"=="3" (
    goto jayhackupdate
    )
  if "%appcontrol%"=="4" (
    goto jayhackuninstall
    )
  if "%appcontrol%"=="5" (
    goto jayhackpullapk
    )

  ::::create function to pull apk file
  :jayhackpullapk
    cls
    Title Pull APK file
    echo ++++++++++++++++++++++++++
    echo Hi  %username%, welcome..
    echo ++++++++++++++++++++++++++
    echo You need the package name to pull the APK file. Put in the APP name to search.
    echo Or "b" to go back.
    echo.
    set /p apksearch=Put in APP name: 
    if "%apksearch%"=="b" (
      goto jayhackappoption
      )
    cls
    echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    adb shell pm list packages | findstr %apksearch%
    echo +++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    echo Copy the package name and place it down below to get the file path.
    echo Or "b" to go back.
    echo.
    echo ++++++++++
    set /p apkfindpath= Put it in: 
    if "%apkfindpath%"=="b" (
      goto jayhackappoption
      )
    cls
    echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    adb shell pm path %apkfindpath%
    echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    echo Apk file path has been located, copy and paste the full path down below to pull it.
    echo Or "b" to go back.
    echo.
    echo ++++++++++
    set /p apkpull= Put it in: 
    if "%apkpull%"=="b" (
      goto jayhackappoption
      )
    cls
    echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    adb pull %apkpull%
    echo ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    rename base.apk %apkfindpath%.apk
    echo Done! Check the jayhack folder for "%apkfindpath%.apk".
    echo.
    echo Input "b" to go back or "1" to pull another APK file.
    echo.
    echo ++++++++++
    set /p apkpullexit= Put it in: 
    if "%apkpullexit%"=="b" (
      goto jayhackappoption
      )
    if "%apkpullexit%"=="1" (
      goto jayhackpullapk
      )
  ::::create function to launch any app
  :jayhacklaunchapp
    cls
    @echo off
    Title Launch an App
    echo ++++++++++++++++++++++++++
    echo Hi  %username%, welcome..
    echo ++++++++++++++++++++++++++
    echo You need the package name to launch an App.
    echo Enter the name to search for the package, "b" to go back.
    echo OR "2" if you already know the package name.
    echo.
    echo ++++++++++
    set /p Lnch=Put it in: 
    if "%lnch%"=="b" (
      goto jayhackappoption
      )
    if "%lnch%"=="2" (
      goto jayhackpack
      )
    cls
    echo ++++++++++++++++++++++++++++++++++++++++++++
    adb shell pm list packages | findstr %lnch%
    echo ++++++++++++++++++++++++++++++++++++++++++++
    echo.
    echo Copy the package name and
    pause
    :jayhackpack
      cls
      echo Pls place the package name down below or "b" to go back.
      set /p lnchapp=Insert package: 
      if "%lnchapp%"=="b" (
        goto jayhacklaunchapp
        )
      adb shell monkey -p %lnchapp% 1
      cls
      echo %lnchapp% has successfully been launched.
      echo To go to the jayhackpage Input "1" or "2" to Launch another App.
      echo.
      echo ++++++++++
      set /p lnchdon=Put it in: 
      if "%lnchdon%"=="1" (
        goto jayhackpage
        )
      if "%lnchdon%"=="2" (
        goto jayhacklaunchapp
        )
  ::::create function to install, uninstall and update an apk.
  :jayhackinstall
    @echo off
    cls
    echo ++++++++++++++++++++++++++
    echo Hi  %username%, welcome..
    echo ++++++++++++++++++++++++++
    Title Install an App
    echo Drag and Drop the apk file here.
    echo.
    echo ++++++++++
    set /p inname=Put it in: 
    cls
    echo Please wait...
    adb install %inname%
    echo.
    echo Input "b" to go back or "1" to install another APP.
    echo.
    echo ++++++++++
    set /p apkpullexit= Put it in: 
    if "%apkpullexit%"=="b" (
      goto jayhackappoption
      )
    if "%apkpullexit%"=="1" (
      goto jayhackinstall
      )

  ::::create a function to update app
  :jayhackupdate
    @echo off
    Title Update an App
    cls
    @echo off
    echo ++++++++++++++++++++++++++
    echo Hi  %username%, welcome..
    echo ++++++++++++++++++++++++++
    echo Drag and Drop the apk file here.
    echo.
    echo ++++++++++
    set /p upname=Put it in: 
    cls
    echo Please wait...
    adb install -r -d %upname%
    echo.
    echo Input "b" to go back or "1" to update another APP.
    echo.
    echo ++++++++++
    set /p apkpullexit= Put it in: 
    if "%apkpullexit%"=="b" (
      goto jayhackappoption
      )
    if "%apkpullexit%"=="1" (
      goto jayhackupdate
      )

  :jayhackuninstall
    @echo off
    Title Uninstall an App
    cls
    @echo off
    echo ++++++++++++++++++++++++++
    echo Hi  %username%, welcome..
    echo ++++++++++++++++++++++++++
    echo You need the package name or title to uninstall.
    echo Please put in the app name to search for the package title Or "2" if you know it.
    echo Put in "b" to go back.
    echo.
    echo ++++++++++
    set /p searchname=Put it in: 
    if "%searchname%"=="b" (
      goto jayhackappoption
      )
    if "%searchname%"=="2" (
      goto uninstallpackage
      )
    cls
    echo ++++++++++++++++++++++++++++++++++++++++++++++++
    adb shell pm list packages | findstr %searchname%
    echo ++++++++++++++++++++++++++++++++++++++++++++++++
    echo Copy the package name and
    pause
    :uninstallpackage
      cls
      echo Put it in the package name to uninstall or "b" to go back.
      echo.
      echo ++++++++++
      set /p packagename=Put it in: 
      if "%packagename%"=="b" goto jayhackuninstall
      cls
      echo Please wait...
      adb uninstall %packagename%
      echo.
      echo Input "b" to go back or "1" to uninstall another APP.
      echo.
      echo ++++++++++
      set /p apkpullexit= Put it in: 
      if "%apkpullexit%"=="b" (
        goto jayhackappoption
        )
      if "%apkpullexit%"=="1" (
        goto jayhackuninstall
        )
