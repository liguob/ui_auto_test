;�ȴ�5�룬���ϴ����ڳ���
WinWait($CmdLine[2],"",10)

;�����뽹�㶨λ���ϴ������ı����У�����ΪEdit,���Ϊ1
ControlFocus($CmdLine[3],"",$CmdLine[4])

;�ж��Ƿ��в���
if $CmdLine[0]>0 Then;�в���
   $file = $CmdLine[1]
;Else���޲���������Ĭ�ϵ��ļ�
   ;$file='D:\work\1.png'
EndIf

;������Ҫ�ϴ����ļ�����·��
ControlSetText($CmdLine[3],"",$CmdLine[4],$file)

;�ȴ��ϴ�ʱ�䣬��λΪ����1��=1000΢�룬���ļ�������Ҫ���õȴ�ʱ��ӳ�
Sleep($CmdLine[6])

;���"��"��ť����������ϴ�����
ControlClick($CmdLine[3],"",$CmdLine[5])