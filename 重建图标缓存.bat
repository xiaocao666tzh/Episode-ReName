@echo off
title �ؽ�ͼ�껺��

:: ��ʾ�û��ر�explorer.exe
echo.
echo ���ͼ��û�и��£����Գ����ؽ�ͼ�껺�档
echo �ù�����Ҫ�ȹر� "Explorer.exe" ���̡�
echo �������������
echo.
pause >nul

:: ���� Explorer ����
echo ���ڹر� Explorer ����...
taskkill /f /im explorer.exe >nul 2>&1
if %errorlevel% neq 0 (
    echo �޷����� Explorer ���̣��������Ѿ��رա�
) else (
    echo Explorer �����ѳɹ��رա�
)

:: ɾ��ͼ�껺���ļ��������ļ�����ʱɾ����
echo ����ɾ��ͼ�껺���ļ�...
set iconCachePath=%localappdata%\Microsoft\Windows\Explorer
if exist "%iconCachePath%\iconcache.db" (
    del /a /f /q "%iconCachePath%\iconcache.db"
    echo iconcache.db �ļ���ɾ����
) else (
    echo û���ҵ� iconcache.db �ļ���
)

for %%F in (%iconCachePath%\thumbcache_*.db) do (
    if exist "%%F" (
        del /a /f /q "%%F"
        echo ��ɾ�� %%F �ļ���
    ) else (
        echo û���ҵ� thumbcache �ļ���
    )
)

:: ���� Explorer ����
echo ������������ Explorer ����...
start explorer.exe

:: �����ʾ
echo.
echo ͼ�껺���ѳɹ��ؽ������Ե�Ƭ�̣�ͼ�꽫�Զ����¡�
timeout /t 5 /nobreak >nul

pause >nul