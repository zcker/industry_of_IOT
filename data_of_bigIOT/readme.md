# introduction

This is a backend programm of processing data that required from bigiot

## services

1. get data via http service
2. store data into mysql
3. send email when sensor report
4. get access_token which can be use for two days and save to token.json

### jsת��ʱ��

function changetime(value) { var secondTime = parseInt(value);// �� var minuteTime = 0;// �� var hourTime = 0;// Сʱ if(
secondTime > 60) {//�����������60��������ת�������� //��ȡ���ӣ�����60ȡ�������õ��������� minuteTime = parseInt(secondTime / 60); //��ȡ����������ȡ�ܣ��õ���������
secondTime = parseInt(secondTime % 60); //������Ӵ���60��������ת����Сʱ if(minuteTime > 60) { //��ȡСʱ����ȡ���ӳ���60���õ�����Сʱ hourTime =
parseInt(minuteTime / 60); //��ȡСʱ��ȡ�ܵķ֣���ȡ���ӳ���60ȡ�ܵķ� minuteTime = parseInt(minuteTime % 60); } } var time = "" +
parseInt(secondTime) + "��";

	        if(minuteTime > 0) {
	        	time = "" + parseInt(minuteTime) + "��" + time;
	        }
	        if(hourTime > 0) {
	        	time = "" + parseInt(hourTime) + "Сʱ" + time;
	        }
	        return time;
	    }