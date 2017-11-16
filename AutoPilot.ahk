; ------------------------------------------------------------------------------
; -------------------------- ED: AUTOPILOT by SKai -----------------------------
; ------------------------------------------------------------------------------

#NoEnv
#Warn
#Persistent
#UseHook
#SingleInstance force
#IfWinActive, Elite - Dangerous (CLIENT)
; AHK Parameters
SetKeyDelay, 0, 50
SendMode Input
SetWorkingDir %A_ScriptDir%
CoordMode Pixel
;set tray icon
if A_IsCompiled {
  Menu, Tray, Icon, %A_ScriptFullPath%, -159
}

; ------------------------------------------------------------------------------
; ------------------------- SECTION ONE: GAME SETTINGS -------------------------
; ----------------You MUST configure these! Modifiers are optional--------------
; ------------------------------------------------------------------------------

; DISPLAY (game must be on borderless window)
; Screen Resolution
Global ScreenX = A_ScreenWidth
Global ScreenY = A_ScreenHeight
; CONTROLS
; Pitch
Global PitchModifierKey := "Alt"
Global PitchUpKey := "w"
Global PitchDownKey := "s"
; Roll
Global RollModifierKey := "lol" ; DO NOT USE
Global RollRightKey := "d"
Global RollLeftKey := "a"
; Yaw
Global YawModifierKey := "Shift"
Global YawRightKey := "d"
Global YawLeftKey := "a"
; Boostv
Global BoostKey := "Tab"
; Throttle 100%
Global SpeedKey := "F5"
; Throttle 0% / Brakes
Global BrakeKey := "space"
; FSD Jump
Global JumpKey := "f"
; Scanning
; --------> must be on mouse left click fire group
; Center Mouse Key
Global CenterJoyKey := "v"
; Galaxy Map
Global GalaxyModifierKey := "g"
Global GalaxyKey := "m"
; Toggle Look Mode Key
Global LookModeKey := "XButton2"

; ------------------------------------------------------------------------------
; ---------------------- SECTION TWO: SHIP CHARACTERISTICS ---------------------
; --------------------------You MUST configure these!---------------------------
; ------------------------------------------------------------------------------

; Ship Parameters
Global Pitch360Time = 25700
Global PitchAccelTime = 200
Global PitchAccelAngle = 2
Global PitchAngularSpeed = % 360 / Pitch360Time
Global PitchAccelVal = % PitchAngularSpeed / PitchAccelTime
Global Roll360Time = 5000
Global RollAccelTime = 1300
Global RollAccelAngle = 1
Global RollAngularSpeed = % 360 / Roll360Time
Global RollAccelVal = % RollAngularSpeed / RollAccelTime
Global Yaw360Time = 55300
Global YawAccelTime = 800
Global YawAccelAngle = 1
Global YawAngularSpeed = % 360 / Yaw360Time
Global YawAccelVal = % YawAngularSpeed / YawAccelTime
Global FSDChargeTime = 15000
Global JumpTime = 18000
Global TimeToRefuel = 90000

; ------------------------------------------------------------------------------
; ----------------- SECTION THREE: AUTOPILOT PROG PARAMETERS -------------------
; --------------------------Configuration is optional---------------------------
; ------------------------------------------------------------------------------

; AutoPilot Toggle
Global AutoPilot = 0
; SuperCruise Variables
Global EscapeTime = 20000
Global ExtraDistance = 0
; Refuel Approach
Global RefuelApproachTime = 4000
; Fuel Gauge Coordinates (Top left of gauge)         ; <---------
Global FuelX = 1896
Global FuelY = 870
; Fuel Gauge Coordinates (Bottom right of gauge)     ; <---------
Global FuelX2 = 2059
Global FuelY2 = 896
Global FuelSearchZone = 10
Global FuelSearchZone2 = 150
; "Align target" Coordinates (top of red triangle)    ; <---------
Global FailX = % (ScreenX / 2) ; 1280
Global FailY = % (ScreenY / 2) - 160 ; 380
Global FailSearchZone = 4
; FSD Cooldown Timer Coordinates (Center of circle)   ; <---------
Global FSDCoolX = 1905
Global FSDCoolY = 940
Global CoolSearchZone = 100
; Other FSD Variables
Global FSDChargeTimeSafety = 2000
; NavPoint offset varaibles
Global OffX = 0
Global OffY = 0
Global NavPointPos = 1
; Routting Variables
Global RouteIndex = 1
Global NextSystem = "Sothis"
; Cake
Global Pi = % ATan(1) * 4
; Config Var
Global ConfigStart = 0

; ------------------------------------------------------------------------------
; -------------------- SECTION FOUR: AUTOPILOT CONTROLS ------------------------
; -----------------You can change the hotkeys here if you like------------------
; ------------------------------------------------------------------------------

; AutoPilot Function
Home::                                    ; <---------
EngageAutoPilot()
return

; Abort / Shutdown Command
End::                                     ; <---------
Abort()
return

PgUp::                                   ; <---------
; Configuration Tool
Configuration()
return

; Configuration Tool
PgDn::                                   ; <---------
Configuration()
return

; Set Destination
Ins::
InsertDestination()
return

; Reset Route
Del::
ResetRoute()
return

F10::
CheckOffSets()
return

; *
; *
; *
; *
; *
; *
; *
; *
; *
; *
; *
; *
; *
; *
; *
; *
; *
; *
; *
; *

; ------------------------------------------------------------------------------
; -------------------- SECTION FIVE: AUTOPILOT PROGAM --------------------------
; -------------Do not change unless you know what you are doing-----------------
; ------------------------------------------------------------------------------

PitchUp(AngleA, InTime = 0) {
  if (AngleA >= 0) {
    Send {%PitchModifierKey% down}
    Send {%PitchUpKey% down}
    if (InTime)
      Sleep, % AngleA
    else {
      if (AngleA > PitchAccelAngle) {
        Sleep, % (AngleA - PitchAccelAngle) / PitchAngularSpeed
      }
      else {
        Sleep, % Sqrt( (2 * AngleA) / PitchAccelVal )
      }
    }
  }
  Send {%PitchUpKey% up}
  Send {%PitchModifierKey% up}
  return
}
PitchDown(AngleA, InTime = 0) {
  if (AngleA >= 0) {
    Send {%PitchModifierKey% down}
    Send {%PitchDownKey% down}
    if (InTime)
      Sleep, % AngleA
    else {
      if (AngleA > PitchAccelAngle) {
        Sleep, % (AngleA - PitchAccelAngle) / PitchAngularSpeed
      }
      else {
        Sleep, % Sqrt( (2 * AngleA) / PitchAccelVal )
      }
    }
  }
  Send {%PitchDownKey% up}
  Send {%PitchModifierKey% up}
  return
}
RollRight(AngleA, InTime = 0) {
  if (AngleA >= 0) {
;    Send {%RollModifierKey% down}
    Send {%RollRightKey% down}
    if (InTime)
      Sleep, % AngleA
    else {
      if (AngleA > RollAccelAngle) {
        Sleep, % (AngleA - RollAccelAngle) / RollAngularSpeed
      }
      else {
        Sleep, % Sqrt( (2 * AngleA) / RollAccelVal )
      }
    }
  }
  Send {%RollRightKey% up}
;  Send {%RollModifierKey% down}
  return
}
RollLeft(AngleA, InTime = 0) {
  if (AngleA >= 0) {
    Send {%RollLeftKey% down}
    if (InTime)
      Sleep, % AngleA
    else {
      if (AngleA > RollAccelAngle) {
        Sleep, % (AngleA - RollAccelAngle) / RollAngularSpeed
      }
      else {
        Sleep, % Sqrt( (2 * AngleA) / RollAccelVal )
      }
    }
  }
  Send {%RollLeftKey% up}
  return
}
YawLeft(AngleA, InTime = 0) {
  if (AngleA >= 0) {
    Send {%YawModifierKey% down}
    Send {a down}
    if (InTime)
      Sleep, % AngleA
    else {
      if (AngleA > YawAccelAngle) {
        Sleep, % (AngleA - YawAccelAngle) / YawAngularSpeed
      }
      else {
        Sleep, % Sqrt( (2 * AngleA) / YawAccelVal )
      }
    }
  }
  Send {a up}
  Send {%YawModifierKey% up}
  return
}
YawRight(AngleA, InTime = 0) {
  if (AngleA >= 0) {
    Send {%YawModifierKey% down}
    Send {%YawRightKey% down}
    if (InTime)
      Sleep, % AngleA
    else {
      if (AngleA > YawAccelAngle) {
        Sleep, % (AngleA - YawAccelAngle) / YawAngularSpeed
      }
      else {
        Sleep, % Sqrt( (2 * AngleA) / YawAccelVal )
      }
    }
  }
  Send {%YawRightKey% up}
  Send {%YawModifierKey% up}
  return
}
Boost() {
  Send {%BoostKey% down}
  Sleep, 50
  Send {%BoostKey% up}
  return
}
Speed() {
  Send {%SpeedKey% down}
  Sleep, 50
  Send {%SpeedKey% up}
  return
}
Brake() {
  Send {%BrakeKey% down}
  Sleep, 100
  Send {%BrakeKey% up}
  return
}
Jump() {
  Send {%JumpKey% down}
  Sleep, 50
  Send {%JumpKey% up}
  return
}
StartScan() {
  Click down
  return
}
EndScan() {
  Click up
  return
}
CenterJoyStick() {
  Send {%CenterJoyKey% down}
  Sleep, 50
  Send {%CenterJoyKey% up}
  return
}
ToggleGalaxyMap() {
  Send {%GalaxyModifierKey% down}
  Sleep, 50
  Send {%GalaxyKey% down}
  Sleep, 50
  Send {%GalaxyKey% up}
  Sleep, 50
  Send {%GalaxyModifierKey% up}
  return
}
ToggleLookMode() {
  Send {%LookModeKey% down}
  Sleep, 50
  Send {%LookModeKey% up}
}

; ------------------------------------------------------------------------------
; ------------------------------------------------------------------------------

Configuration() {
  LoadSettings()
  LoadRoutePos()
  ConfigStart = 1
  Advise("Configuration Started", 2)
  Advise("To skip a setting press cancel", 3)

  Advise("Set re-fuel approach time",0)
  InputBox, RefuelApproachTime, Re-Fuel Approach Time in ms ,,, 250 , 100 , (ScreenX / 2)-125 , (ScreenY / 2) ,,, %RefuelApproachTime%
  Sleep, 200

  Advise("Input time to fully refuel ship",0)
  InputBox, TimeToRefuel, Refuel time in ms ,,, 250 , 100 , (ScreenX / 2)-125 , (ScreenY / 2) ,,, %TimeToRefuel%
  Sleep, 200

  Advise("Input jump time",0)
  InputBox, JumpTime, Jump Time in ms ,,, 250 , 100 , (ScreenX / 2)-125 , (ScreenY / 2) ,,, %JumpTime%
  Sleep, 200

  MsgBox, 1, Coordinates, Set Fuel Gauge Coordinates?
  IfMsgBox OK
  {
    Sleep, 100
    Advise("Click on the top left of the fuel gauge",0)
    KeyWait, LButton, D
    MouseGetPos, MX, MY
    MsgBox, 1, Confirm Coordinates? , % "(" . MX . "," . MY . ")"
    IfMsgBox OK
    {
      FuelX = % MX
      FuelY = % MY
    }
    Advise("",0)
    Sleep, 200

    Advise("Click on the bottom right of the fuel gauge",0)
    KeyWait, LButton, D
    MouseGetPos, MX, MY
    MsgBox, 1, Confirm Coordinates? , % "(" . MX . "," . MY . ")"
    IfMsgBox OK
    {
      FuelX2 = % MX
      FuelY2 = % MY
    }
    Advise("",0)
  }
  Sleep, 200

  MsgBox, 1, Coordinates, Set Align Target Alert Coordinates?
  IfMsgBox OK
  {
    Sleep, 100
    Advise("Click on the top of the ""Align Target"" alert",0)
    KeyWait, LButton, D
    MouseGetPos, MX, MY
    MsgBox, 1, Confirm Coordinates? , % "(" . MX . "," . MY . ")"
    IfMsgBox OK
    {
      FailX = % MX
      FailY = % MY
    }
    Advise("",0)
  }
  Sleep, 200

  Advise("Input time to Pitch 360 degrees",0)
  InputBox, Pitch360Time, Pitch 360 time in ms ,,, 250 , 100 , (ScreenX / 2)-125 , (ScreenY / 2) ,,, %Pitch360Time%
  Sleep, 200

  Advise("Input Pitch acceleration",0)
  InputBox, PitchAccelTime, Pitch acceleration time in ms ,,, 250 , 100 , (ScreenX / 2)-125 , (ScreenY / 2) ,,, %PitchAccelTime%
  Sleep, 200

  Advise("Input time to Roll 360 degrees",0)
  InputBox, Roll360Time, Roll 360 time in ms ,,, 250 , 100 , (ScreenX / 2)-125 , (ScreenY / 2) ,,, %Roll360Time%
  Sleep, 200

  Advise("Input Roll acceleration",0)
  InputBox, RollAccelTime, Roll acceleration time in ms ,,, 250 , 100 , (ScreenX / 2)-125 , (ScreenY / 2) ,,, %RollAccelTime%
  Sleep, 200

  Advise("Input time to Yaw 360 degrees",0)
  InputBox, Yaw360Time, Yaw 360 time in ms ,,, 250 , 100 , (ScreenX / 2)-125 , (ScreenY / 2) ,,, %Yaw360Time%
  Sleep, 200

  Advise("Input Yaw acceleration",0)
  InputBox, YawAccelTime, Yaw acceleration time in ms ,,, 250 , 100 , (ScreenX / 2)-125 , (ScreenY / 2) ,,, %YawAccelTime%
  Sleep, 200

  SaveSettings()
  SaveRoutePos()
  ConfigStart = 0
  Advise("Configuration complete", 2)
  return
}

CheckOffSets() {
  FindNavPointOffset()
  MsgBox, %OffX%x%OffY%
  return
}

Abort() {
  if ( ConfigStart = 0 )
    LoadSettings()
  else
    ConfigStart = 0
  LoadRoutePos()
  Advise("Aborting", 1)
  AutoPilot = 0
  ShutOff()
  SaveSettings()
  SaveRoutePos()
  Reload
  return
}

Advise(content, TimeS) {
; ToolTipColor(0x000000,0xFF841E)
;  WinSet, TransColor, 0x000000
  Tooltip, % " " . content . " ", 5, 15
  WinGetPos, X,Y,W,H, ahk_class tooltips_class32
  ToolTip, % " " . content . " ", (ScreenX / 2)-(W / 2) , (ScreenY / 6)
  if (TimeS > 0) {
    Sleep, % TimeS * 1000
    ToolTip
  }
  return
}

; ------------------------------------------------------------------------------
; ------------------------------------------------------------------------------

SaveRoutePos() {
  FileReadLine, Index, Data/RouteIndex.txt, 1
  if (ErrorLevel = 0) {
    FileRecycle, Data/RouteIndex.txt
  }
  FileAppend, %RouteIndex% , Data/RouteIndex.txt
  return
}

LoadRoutePos() {
  FileReadLine, Index, Data/RouteIndex.txt, 1
  if (ErrorLevel = 0) {
    RouteIndex = %Index%
  }
  return
}

SaveSettings() {
  FileReadLine, Test, Settings.txt, 1
  if (ErrorLevel = 0) {
    FileRecycle, Settings.txt
  }
  ; GAME SETTINGS
  FileAppend, -`n , Settings.txt
  FileAppend, -`n , Settings.txt
  FileAppend, %PitchModifierKey%`n , Settings.txt
  FileAppend, %PitchUpKey%`n , Settings.txt
  FileAppend, %PitchDownKey%`n , Settings.txt
  FileAppend, %RollModifierKey%`n , Settings.txt
  FileAppend, %RollRightKey%`n , Settings.txt
  FileAppend, %RollLeftKey%`n , Settings.txt
  FileAppend, %YawModifierKey%`n , Settings.txt
  FileAppend, %YawRightKey%`n , Settings.txt
  FileAppend, %YawLeftKey%`n , Settings.txt
  FileAppend, %BoostKey%`n , Settings.txt
  FileAppend, %SpeedKey%`n , Settings.txt
  FileAppend, %BrakeKey%`n , Settings.txt
  FileAppend, %JumpKey%`n , Settings.txt
  FileAppend, %CenterJoyKey%`n , Settings.txt
  FileAppend, %GalaxyModifierKey%`n , Settings.txt
  FileAppend, %GalaxyKey%`n , Settings.txt
  ; SHIP CHARACTERISTICS
  FileAppend, %Pitch360Time%`n , Settings.txt
  FileAppend, %PitchAccelTime%`n , Settings.txt
  FileAppend, %PitchAccelAngle%`n , Settings.txt
  FileAppend, %PitchAccelVal%`n , Settings.txt
  FileAppend, %Roll360Time%`n , Settings.txt
  FileAppend, %RollAccelTime%`n , Settings.txt
  FileAppend, %RollAccelAngle%`n , Settings.txt
  FileAppend, %RollAccelVal%`n , Settings.txt
  FileAppend, %Yaw360Time%`n , Settings.txt
  FileAppend, %YawAccelTime%`n , Settings.txt
  FileAppend, %YawAccelAngle%`n , Settings.txt
  FileAppend, %YawAccelVal%`n , Settings.txt
  FileAppend, %FSDChargeTime%`n , Settings.txt
  FileAppend, %JumpTime%`n , Settings.txt
  FileAppend, %TimeToRefuel%`n , Settings.txt
  ; PROGRAM PARAMETERS
  FileAppend, %EscapeTime%`n , Settings.txt
  FileAppend, %ExtraDistance%`n , Settings.txt
  FileAppend, -`n , Settings.txt
  FileAppend, -`n , Settings.txt
  FileAppend, -`n , Settings.txt
  FileAppend, -`n , Settings.txt
  FileAppend, -`n , Settings.txt
  FileAppend, -`n , Settings.txt
  FileAppend, -`n , Settings.txt
  FileAppend, -`n , Settings.txt
  FileAppend, %FuelX%`n , Settings.txt
  FileAppend, %FuelY%`n , Settings.txt
  FileAppend, %FuelX2%`n , Settings.txt
  FileAppend, %FuelY2%`n , Settings.txt
  FileAppend, %FuelSearchZone%`n , Settings.txt
  FileAppend, %FuelSearchZone2%`n , Settings.txt
  FileAppend, %RefuelApproachTime%`n , Settings.txt
  FileAppend, %FailX%`n , Settings.txt
  FileAppend, %FailY%`n , Settings.txt
  FileAppend, %FailSearchZone%`n , Settings.txt
  FileAppend, -`n , Settings.txt
  FileAppend, -`n , Settings.txt
  FileAppend, -`n , Settings.txt
  FileAppend, %FSDChargeTimeSafety%`n , Settings.txt
  return
}

LoadSettings() {
  FileReadLine, Test, Settings.txt, 1
  if (ErrorLevel != 0) {
    return
  }
  LineCount = 1
  ; GAME SETTINGS
  LineCount++
  LineCount++
  FileReadLine, PitchModifierKey , Settings.txt, LineCount++
  FileReadLine, PitchUpKey , Settings.txt, LineCount++
  FileReadLine, PitchDownKey , Settings.txt, LineCount++
  FileReadLine, RollModifierKey , Settings.txt, LineCount++
  FileReadLine, RollRightKey , Settings.txt, LineCount++
  FileReadLine, RollLeftKey , Settings.txt, LineCount++
  FileReadLine, YawModifierKey , Settings.txt, LineCount++
  FileReadLine, YawRightKey , Settings.txt, LineCount++
  FileReadLine, YawLeftKey , Settings.txt, LineCount++
  FileReadLine, BoostKey , Settings.txt, LineCount++
  FileReadLine, SpeedKey , Settings.txt, LineCount++
  FileReadLine, BrakeKey , Settings.txt, LineCount++
  FileReadLine, JumpKey , Settings.txt, LineCount++
  FileReadLine, CenterJoyKey , Settings.txt, LineCount++
  FileReadLine, GalaxyModifierKey , Settings.txt, LineCount++
  FileReadLine, GalaxyKey , Settings.txt, LineCount++
  ; SHIP CHARACTERISTICS
  FileReadLine, Pitch360Time , Settings.txt, LineCount++
  FileReadLine, PitchAccelTime , Settings.txt, LineCount++
  FileReadLine, PitchAccelAngle , Settings.txt, LineCount++
  FileReadLine, PitchAccelVal , Settings.txt, LineCount++
  FileReadLine, Roll360Time , Settings.txt, LineCount++
  FileReadLine, RollAccelTime , Settings.txt, LineCount++
  FileReadLine, RollAccelAngle , Settings.txt, LineCount++
  FileReadLine, RollAccelVal , Settings.txt, LineCount++
  FileReadLine, Yaw360Time , Settings.txt, LineCount++
  FileReadLine, YawAccelTime , Settings.txt, LineCount++
  FileReadLine, YawAccelAngle , Settings.txt, LineCount++
  FileReadLine, YawAccelVal , Settings.txt, LineCount++
  FileReadLine, FSDChargeTime , Settings.txt, LineCount++
  FileReadLine, JumpTime , Settings.txt, LineCount++
  FileReadLine, TimeToRefuel , Settings.txt, LineCount++
  ; PROGRAM PARAMETERS
  FileReadLine, EscapeTime , Settings.txt, LineCount++
  FileReadLine, ExtraDistance , Settings.txt, LineCount++
  LineCount++
  LineCount++
  LineCount++
  LineCount++
  LineCount++
  LineCount++
  LineCount++
  LineCount++
  FileReadLine, FuelX , Settings.txt, LineCount++
  FileReadLine, FuelY , Settings.txt, LineCount++
  FileReadLine, FuelX2 , Settings.txt, LineCount++
  FileReadLine, FuelY2 , Settings.txt, LineCount++
  FileReadLine, FuelSearchZone , Settings.txt, LineCount++
  FileReadLine, FuelSearchZone2 , Settings.txt, LineCount++
  FileReadLine, RefuelApproachTime , Settings.txt, LineCount++
  FileReadLine, FailX , Settings.txt, LineCount++
  FileReadLine, FailY , Settings.txt, LineCount++
  FileReadLine, FailSearchZone , Settings.txt, LineCount++
  LineCount++
  LineCount++
  LineCount++
  FileReadLine, FSDChargeTimeSafety , Settings.txt, LineCount++
  return
}

; ------------------------------------------------------------------------------
; ------------------------------------------------------------------------------

EngageAutoPilot() {
  LoadSettings()
  LoadRoutePos()
  Advise("AutoPilot Engaged", 1)
  AutoPilot = 1
  while (AutoPilot) {
    CheckRoute()
    AlignShip()
    InitiateJump()
    FinishJump()
    CheckFuel()
    GoSafeDistance()
  }
  SaveSettings()
  SaveRoutePos()
  ShutOff()
  return
}

; ------------------------------------------------------------------------------
; ------------------------------------------------------------------------------

InsertDestination() {
  Advise("Insert Destination",1)
  InputBox, NextSystem, AutoPilot - Insert Destination, ,, 370 , 100 , (ScreenX / 2)-185 , (ScreenY / 6) + 20 , ,
  if (ErrorLevel) {
    Advise("Canceled",1)
    return
  }
  if (PlotNextBlock() = 1) {
    EngageAutoPilot()
  }
  else {
    Advise("Plotting Failed", 1)
    Abort()
  }
  return
}

HaveTarget() {
  FoundCount = 0
  Loop, 10 {
    RunWait, %comspec% /c ""Data/GetNavPointOffset/GetNavPointOffset.exe" > "Data/NavPoint.txt"" ,, Hide UseErrorLevel  }
    FileReadLine, NavPointPos, Data/NavPoint.txt, 1
    if (NavPointPos >= 0) {
      FoundCount++
    }
  }
  if (FoundCount > 5)
    return 1
  else
    return 0
}

CheckRoute() {
  Advise("Routing", 0)
  if (HaveTarget() = 0) {
    if (GetNextSystem() = 0) {
        Advise("Route Complete",1)
        Abort()
    }
    else if (PlotNextBlock() = 1) {
      RouteIndex++
    }
    else {
      Advise("Plotting Failed", 1)
      ToggleGalaxyMap()
      Abort()
    }
  }
  return
}

ResetRoute() {
  Advise("Reseting Route",1)
  RouteIndex = 1
  SaveRoutePos()
  return
}

GetNextSystem() {
  FileReadLine, NextSystem, Data/Route.txt, RouteIndex
  if (ErrorLevel = 0 && RouteIndex > 1) {
    return 1
  }
  else {
    return 0
  }
}

PlotNextBlock() {
    Advise("Plotting Next Block",1)
    PlotCount = 0
    Sleep, 100
    ToggleGalaxyMap()
    ImageSearch, BX, BY, 0, 0, ScreenX / 3 , ScreenY / 2, *50 Data/RouteButton1.png
    while (ErrorLevel) {
      PlotCount++
      if (PlotCount > 40) {
        return 0
      }
      Sleep, 100
      ImageSearch, BX, BY, 0, 0, ScreenX / 3 , ScreenY / 2, *50 Data/RouteButton1.png
    }
    PlotCount = 0
    MouseHere(BX , BY, 1)

    ImageSearch, BX, BY, 0, 0, ScreenX / 2 , ScreenY / 2, *50 Data/RouteSearchBar.png
    if (ErrorLevel) {
      ImageSearch, BX, BY, 0, 0, ScreenX / 2 , ScreenY / 2, *50 Data/RouteSearchBar2.png
    }
    while (ErrorLevel) {
      PlotCount++
      if (PlotCount > 40) {
        return 0
      }
      Sleep, 100
      ImageSearch, BX, BY, 0, 0, ScreenX / 2 , ScreenY / 2, *50 Data/RouteSearchBar.png
      if (ErrorLevel) {
        ImageSearch, BX, BY, 0, 0, ScreenX / 2 , ScreenY / 2, *50 Data/RouteSearchBar2.png
      }
    }
    PlotCount = 0
    MouseHere(BX , BY, 1)

    Send %NextSystem%
    Sleep, 1000
    Send {enter down}
    Sleep, 100
    Send {enter up}
    MouseHere(ScreenX / 2 , ScreenY / 2 , 0)

    ImageSearch, BX, BY, ScreenX / 3 , ScreenY / 3 , ScreenX * 2 / 3 , ScreenY * 2 / 3 , *50 Data/RouteButton2.png
    if (ErrorLevel) {
      ImageSearch, BX, BY, ScreenX / 3 , ScreenY / 3 , ScreenX * 2 / 3 , ScreenY * 2 / 3 , *50 Data/RouteButton2-2.png
      if (ErrorLevel) {
        ImageSearch, BX, BY, ScreenX / 3 , ScreenY / 3 , ScreenX * 2 / 3 , ScreenY * 2 / 3 , *25 Data/LRRouteButton1.png
        if (ErrorLevel) {
          ImageSearch, BX, BY, ScreenX / 3 , ScreenY / 3 , ScreenX * 2 / 3 , ScreenY * 2 / 3 , *25 Data/LRRouteButton2.png
          if (ErrorLevel = 0) {
            return LongRangeRoute()
          }
        }
        else {
          return LongRangeRoute()
        }
      }
    }
    while (ErrorLevel) {
      PlotCount++
      if (PlotCount > 40) {
        return 0
      }
      Sleep, 100
      ImageSearch, BX, BY, ScreenX / 3 , ScreenY / 3 , ScreenX * 2 / 3 , ScreenY * 2 / 3 , *50 Data/RouteButton2.png
      if (ErrorLevel) {
        ImageSearch, BX, BY, ScreenX / 3 , ScreenY / 3 , ScreenX * 2 / 3 , ScreenY * 2 / 3 , *50 Data/RouteButton2-2.png
        if (ErrorLevel) {
          ImageSearch, BX, BY, ScreenX / 3 , ScreenY / 3 , ScreenX * 2 / 3 , ScreenY * 2 / 3 , *25 Data/LRRouteButton1.png
          if (ErrorLevel) {
            ImageSearch, BX, BY, ScreenX / 3 , ScreenY / 3 , ScreenX * 2 / 3 , ScreenY * 2 / 3 , *25 Data/LRRouteButton2.png
            if (ErrorLevel = 0) {
              return LongRangeRoute()
            }
          }
          else {
            return LongRangeRoute()
          }
        }
      }
    }
    PlotCount = 0
    MouseHere(BX , BY, 1)

    Sleep, 1000
    ToggleGalaxyMap()
    Sleep, 4000
    return 1
}

LongRangeRoute() {
  Sleep, 500
  Advise("Setting Long Range Route",0)
  InputBox, OriginSystem, AutoPilot - Insert Origin, ,, 370 , 100 , (ScreenX / 2)-185 , (ScreenY / 6) + 20 , ,
  if (ErrorLevel) {
    Advise("Canceled",1)
    return 0
  }
  DestinationSystem = %NextSystem%
  FileReadLine, test, Data/LRRoute.txt, 1
  if (ErrorLevel = 0) {
    FileRecycle, Data/LRRoute.txt
  }
  RunWait, %comspec% /c ""Data/ED-FastTravel.exe" "%OriginSystem%" "%DestinationSystem%" "20000" > "Data/LRRoute.txt"" ,, UseErrorLevel
  FileReadLine, test, Data/Route.txt, 1
  if (ErrorLevel = 0) {
    FileRecycle, Data/Route.txt
  }
  Loop, read, Data/LRRoute.txt
  {
    IfInString, A_LoopReadLine, '
    {
      Pos1 := InStr(A_LoopReadLine, "'" ,,, 1 ) + 1
      Pos2 := InStr(A_LoopReadLine, "'" ,,, 2 )
      System := SubStr(A_LoopReadLine, Pos1 , Pos2 - Pos1)
      FileAppend, %System%`n , Data/Route.txt
    }
  }
  RouteIndex = 2
  SaveRoutePos()
  Advise("Long Range Route Calculated", 1)
  ToggleGalaxyMap()
  Sleep, 4000
  return 1
}

MouseHere(CX, CY, click) {
  SendMode Event
  Sleep, 200
  MouseMove, CX + 5 , CY + 5 , 15
  if (click) {
    Sleep, 200
    Click down
    Sleep, 200
    Click up
  }
  Sleep, 200
  SendMode Input
  return
}

; ------------------------------------------------------------------------------
; ------------------------------------------------------------------------------

FindNavPointOffset() {
  SampleCount = 0
  NX = 0
  NY = 0
  NavPointPos = -1

  Loop, 3 {
    RunWait, %comspec% /c ""Data/GetNavPointOffset/GetNavPointOffset.exe" > "Data/NavPoint.txt"" ,, Hide UseErrorLevel  }
    FileReadLine, NavPointPos, Data/NavPoint.txt, 1
    if (NavPointPos >= 0) {
      FileReadLine, TX, Data/NavPoint.txt, 2
      FileReadLine, TY, Data/NavPoint.txt, 3
      NX = % NX + TX
      NY = % NY + TY
      SampleCount++
    }
  }
  ; Calculate Offset
  if (SampleCount > 0) {
    OffX = % NX / SampleCount
    OffY = % NY / SampleCount
    return 1
  }
  else {
    OffX = 15
    OffY = 15
    return 0
  }
}

AlignShip() {
  ThresholdX = 2
  ThresholdY = 2
  ThresMult = 3
  AngleMultRoll = 1
  AngleMultPitch = 1

  Sleep, 50
  Advise("Aligning Ship", 0)
  ; Phase 0 - NavPoint hidden
  while (FindNavPointOffset() = 0) {
    RollRight(5)
    PitchUp(5)
    Sleep, 50
  }
  ; Phase 1 Crude
  while (NavPointPos = 0 OR OffX > ThresholdX * ThresMult OR OffX < -ThresholdX * ThresMult OR OffY > ThresholdY * ThresMult OR OffY < -ThresholdY * ThresMult) {
    FindNavPointOffset()
    TempValX = % Abs(OffX)
    TempValY = % Abs(OffY)
    ; Roll Angle
    RollAngle = % ATan( TempValY / TempValX )
    RollAngle = % RollAngle * 180 / Pi
    if (OffY > 0)
      RollAngle = % 90 - RollAngle
    else
      RollAngle = % 90 + RollAngle
    ; Pitch Angle
    PitchDistance = % Sqrt(TempValX * TempValX + TempValY * TempValY)
    PitchAngle = % ASin( PitchDistance / (ScreenY / 36) )
    PitchAngle = % PitchAngle * 180 / Pi
    if (NavPointPos = 0)
      PitchAngle = % PitchAngle + (( 90 - PitchAngle) * 2 )
    ; Movement
    if (OffX > ThresholdX * ThresMult)
      RollRight(RollAngle)
    else if (OffX < -ThresholdX * ThresMult)
      RollLeft(RollAngle)
    else if (TempValY > ThresholdY * ThresMult && NavPointPos = 0)
      RollRight(RollAngle)
    if (PitchDistance > ThresholdY * ThresMult OR NavPointPos = 0)
      PitchUp(PitchAngle)
    Sleep, 50
  }
  ; Phase 2 Fine
  StepDefH = 4
  StepDefL = 2
  Step = % StepDefH
  StepCount = 0
  FindNavPointOffset()
  while ( (OffX > 0 + ThresholdX) OR (OffX < 0 - ThresholdX) OR (OffY > 0 + ThresholdY) OR (OffY < 0 - ThresholdY) ) {
    if (OffX > 0 + ThresholdX) {
      YawRight(Step)
    }
    else if (OffX < 0 - ThresholdX) {
      YawLeft(Step)
    }

    if (OffY > 0 + ThresholdY) {
      PitchUp(Step)
    }
    else if (OffY < 0 - ThresholdY) {
      PitchDown(Step)
    }
    StepCount++
    if (Mod(StepCount, 2) = 0) {
      Step = % StepDefH
    }
    else {
      Step = % StepDefL
    }
    Sleep, 50
    FindNavPointOffset()
  }
  Advise("",0)
  return
}

; ------------------------------------------------------------------------------
; ------------------------------------------------------------------------------

InitiateJump() {
  Advise("Jump", 0)
  Speed()
  Jump() ; Start Jump
  Sleep, % FSDChargeTime + FSDChargeTimeSafety
  if (JumpFailed() = 1) {
    Advise("Alignment Fail", 0)
    Brake()
    Jump() ; Stop Jump
    Sleep, 4000
    Advise("", 0)
    AlignShip() ; Attempt Realign
    InitiateJump()
  }
  return
}

JumpFailed() {
  FailCount = 0v
  Loop, 20 {
    PixelSearch, FX, FY, FailX-FailSearchZone, FailY-FailSearchZone, FailX+FailSearchZone, FailY+FailSearchZone, 0xE10803 , 50 , RGB Fast
    if (ErrorLevel = 0) {
      return 1
    }
    Sleep, 100
  }
  return 0
}

FinishJump() {
  Sleep, 10000
  BrakeTime = % JumpTime - FSDChargeTimeSafety - 10000
  CountTime = 0
  while (CountTime < BrakeTime) {
    Sleep, 500
    Brake()
    CountTime = % CountTime + 500
  }
  FailCount = 0
  while (HaveTarget() = 0) {
    FailCount++
    Sleep, 100
    Brake()
    if (FailCount > 40)
      Advise("Navigation Error", 2)
      Abort()
  }
  Advise("Full Stop", 0)
  Loop, 5 {
    Brake()
    Sleep, 200
  }
  Advise("",0)
  return
}

; ------------------------------------------------------------------------------
; ------------------------------------------------------------------------------

CheckFuel() {
  Loop, 10 {
    PixelSearch, FX, FY, FuelX - 20 , FuelY - 50 , FuelX + (FuelX2 - FuelX) /  4 , FuelY2 + 35 , 0xC3D6FF, 35, RGB Fast
    if (ErrorLevel = 0) {
      Refuel()
    }
    Sleep, 50
  }
  return
}

Refuel() {
  Advise("Refuel", 0)
  ExtraDistance = 10000
  Speed()
  Sleep, % RefuelApproachTime
  Brake()
  Sleep, % TimeToRefuel * 3 / 4
  Advise("", 0)
  return
}

; ------------------------------------------------------------------------------
; ------------------------------------------------------------------------------

GoSafeDistance() {
  NumBlocks = 15
  Num1 = % NumBlocks / 3
  Num2 = % (NumBlocks / 3)*2
  Num3 = % (NumBlocks / 3)*3
  BlockX = % ScreenX / NumBlocks
  BlockY = % ScreenY / NumBlocks
  BX = 1
  BY = 1
  CountR1 = 0
  CountR2 = 0
  CountR3 = 0
  CountR4 = 0
  CountR5 = 0
  CountR6 = 0
  CountR7 = 0
  CountR8 = 0
  CountR9 = 0
  MaxCount = % 0
  SafeRegion = 0
  Advise("Scan and Reposition", 0)
  StartScan()
  ; Region 1
  while (BX <= Num1) {
    while (BY <= Num1) {
      PixelSearch, PointX, PointY, (BX - 1)*BlockX, (BY - 1)*BlockY, BX*BlockX, BY*BlockY, 0x000000, 0, RGB Fast
      if (ErrorLevel = 0) {
        CountR1++
      }
      BY++
    }
    BY = 1
    BX++
  }
  SafeRegion = 1

  ; Region 2
  BX = % Num1 + 1
  BY = 1
  while (BX <= Num2) {
    while (BY <= Num1) {
      PixelSearch, PointX, PointY, (BX - 1)*BlockX, (BY - 1)*BlockY, BX*BlockX, BY*BlockY, 0x000000, 0, RGB Fast
      if (ErrorLevel = 0) {
        CountR2++
      }
      BY++
    }
    BY = 1
    BX++
  }
  if (CountR2 > CountR1) {
    MaxCount = % CountR2
    SafeRegion = 2
  }

  ; Region 3
  BX = % Num2 + 1
  BY = 1
  while (BX <= Num2) {
    while (BY <= Num2) {
      PixelSearch, PointX, PointY, (BX - 1)*BlockX, (BY - 1)*BlockY, BX*BlockX, BY*BlockY, 0x000000, 0, RGB Fast
      if (ErrorLevel = 0) {
        CountR3++
      }
      BY++
    }
    BY = 1
    BX++
  }
  if (CountR3 > MaxCount) {
    MaxCount = % CountR3
    SafeRegion = 3
  }

  ; Region 4
  BX = 1
  BY = % Num1 + 1
  while (BX <= Num1) {
    while (BY <= Num2) {
      PixelSearch, PointX, PointY, (BX - 1)*BlockX, (BY - 1)*BlockY, BX*BlockX, BY*BlockY, 0x000000, 0, RGB Fast
      if (ErrorLevel = 0) {
        CountR4++
      }
      BY++
    }
    BY = % Num1 + 1
    BX++
  }
  if (CountR4 > MaxCount) {
    MaxCount = % CountR4
    SafeRegion = 4
  }

  ; Region 5
  BX = % Num1 + 1
  BY = % Num1 + 1
  while (BX <= Num2) {
    while (BY <= Num2) {
      PixelSearch, PointX, PointY, (BX - 1)*BlockX, (BY - 1)*BlockY, BX*BlockX, BY*BlockY, 0x000000, 0, RGB Fast
      if (ErrorLevel = 0) {
        CountR4++
      }
      BY++
    }
    BY = % Num1 + 1
    BX++
  }
  if (CountR5 > MaxCount) {
    MaxCount = % CountR5
    SafeRegion = 5
  }

  ; Region 6
  BX = % Num2 + 1
  BY = % Num1 + 1
  while (BX <= Num3) {
    while (BY <= Num3) {
      PixelSearch, PointX, PointY, (BX - 1)*BlockX, (BY - 1)*BlockY, BX*BlockX, BY*BlockY, 0x000000, 0, RGB Fast
      if (ErrorLevel = 0) {
        CountR6++
      }
      BY++
    }
    BY = % Num1 + 1
    BX++
  }
  if (CountR6 > MaxCount) {
    MaxCount = % CountR6
    SafeRegion = 6
  }

  ; Region 7
  BX = 1
  BY = % Num2 + 1
  while (BX <= Num1) {
    while (BY <= Num3) {
      PixelSearch, PointX, PointY, (BX - 1)*BlockX, (BY - 1)*BlockY, BX*BlockX, BY*BlockY, 0x000000, 0, RGB Fast
      if (ErrorLevel = 0) {
        CountR4++
      }
      BY++
    }
    BY = % Num2 + 1
    BX++
  }
  if (CountR7 > MaxCount) {
    MaxCount = % CountR7
    SafeRegion = 7
  }

  ; Region 8
  BX = % Num1 + 1
  BY = % Num2 + 1
  while (BX <= Num2) {
    while (BY <= Num3) {
      PixelSearch, PointX, PointY, (BX - 1)*BlockX, (BY - 1)*BlockY, BX*BlockX, BY*BlockY, 0x000000, 0, RGB Fast
      if (ErrorLevel = 0) {
        CountR8++
      }
      BY++
    }
    BY = % Num2 + 1
    BX++
  }
  if (CountR8 > MaxCount) {
    MaxCount = % CountR8
    SafeRegion = 8
  }

  ; Region 9
  BX = % Num2 + 1
  BY = % Num2 + 1
  while (BX <= Num3) {
    while (BY <= Num3) {
      PixelSearch, PointX, PointY, (BX - 1)*BlockX, (BY - 1)*BlockY, BX*BlockX, BY*BlockY, 0x000000, 0, RGB Fast
      if (ErrorLevel = 0) {
        CountR9++
      }
      BY++
    }
    BY = % Num2 + 1
    BX++
  }
  if (CountR9 > MaxCount) {
    MaxCount = % CountR9
    SafeRegion = 9
  }

  EscapePitch = 95
  if (ExtraDistance != 0) {
    TimeToRun = % EscapeTime + ExtraDistance
    ExtraDistance = 0
  }
  else {
    TimeToRun = % EscapeTime
  }
  if (SafeRegion = 1) {
    RollLeft(45)
    PitchUp(EscapePitch)
  }
  else if (SafeRegion = 2) {
    PitchUp(EscapePitch)
  }
  else if (SafeRegion = 3) {
    RollRight(45)
    PitchUp(EscapePitch)
  }
  else if (SafeRegion = 4) {
    RollLeft(90)
    PitchUp(EscapePitch)
  }
  else if (SafeRegion = 5) {
  }
  else if (SafeRegion = 6) {
    RollRight(90)
    PitchUp(EscapePitch)
  }
  else if (SafeRegion = 7) {
    RollLeft(135)
    PitchUp(EscapePitch)
  }
  else if (SafeRegion = 8) {
    RollLeft(180)
    PitchUp(EscapePitch)
  }
  else if (SafeRegion = 9) {
    RollRight(135)
    PitchUp(EscapePitch)
  }
  Boost()
  Speed()
  EndScan()
  Sleep, TimeToRun
  Brake()
  RollRight(150)
  PitchUp(EscapePitch)
  Advise("",0)
  return
}

; ------------------------------------------------------------------------------
; ------------------------------------------------------------------------------

ShutOff() {
  CenterJoyStick()
  Brake()
  EndScan()
  PitchUp(-1)
  PitchDown(-1)
  RollRight(-1)
  RollLeft(-1)
  YawRight(-1)
  YawLeft(-1)
  return
}
