;等待5秒，让上传窗口出现
WinWait($CmdLine[2],"",10)

;把输入焦点定位到上传输入文本框中，类型为Edit,编号为1
ControlFocus($CmdLine[3],"",$CmdLine[4])

;判断是否有参数
if $CmdLine[0]>0 Then;有参数
   $file = $CmdLine[1]
;Else：无参数，传递默认的文件
   ;$file='D:\work\1.png'
EndIf

;输入需要上传的文件绝对路径
ControlSetText($CmdLine[3],"",$CmdLine[4],$file)

;等待上传时间，单位为毫秒1秒=1000微秒，如文件过大需要设置等待时间加长
Sleep($CmdLine[6])

;点击"打开"按钮，完成整个上传过程
ControlClick($CmdLine[3],"",$CmdLine[5])