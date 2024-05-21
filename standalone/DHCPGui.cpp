
// based on https://msdn.microsoft.com/en-us/library/ms682425%28VS.85%29.aspx
// can be compiled with https://bloodshed.net/ DevC++ 5

#include <windows.h>
#include <stdio.h>
#include <tchar.h>

int _tmain( int argc, TCHAR *argv[] )
{
    STARTUPINFO si;
    PROCESS_INFORMATION pi;
    TCHAR command[] = "\"Portable Python 3\\App\\pythonw.exe\" \"dhcpgui.pyw\"";
    TCHAR directory[] = "server";

    ZeroMemory( &si, sizeof(si) );
    si.cb = sizeof(si);
    ZeroMemory( &pi, sizeof(pi) );

    // Start the child process. 
    if( !CreateProcess( NULL,   // No module name (use command line)
        command,        // Command line
        NULL,           // Process handle not inheritable
        NULL,           // Thread handle not inheritable
        FALSE,          // Set handle inheritance to FALSE
        0,              // No creation flags
        NULL,           // Use parent's environment block
        directory,           // Use parent's starting directory 
        &si,            // Pointer to STARTUPINFO structure
        &pi )           // Pointer to PROCESS_INFORMATION structure
    ) 
    {
        printf( "CreateProcess failed (%d).\n", GetLastError() );
        return 1;
    }
/*
    // Wait until child process exits.
    WaitForSingleObject( pi.hProcess, INFINITE );

    // Close process and thread handles. 
    CloseHandle( pi.hProcess );
    CloseHandle( pi.hThread );
*/
    return 0;
}
