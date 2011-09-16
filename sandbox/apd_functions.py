from replacement import execute, shell_exec, system, passthru, popen

FUNCTIONS = {
             "getcwd;" : "\treturn '%s';" % "/var/www", 
             "php_uname;" : "\treturn '%s';" % "Linux Server 2.6.38-11-generic #49-Ubuntu SMP Mon Aug 29 20:47:58 UTC 2011 i686", 
             "ini_get;" : "\treturn '%s';" % "", 
             "disk_free_space;" : "\treturn '%s';" % "36698988544", 
             "disk_total_space;" : "\treturn '%s';" % "51221590016", 
             "diskfreespace;" : "\treturn '%s';" % "36698988544", 
             "exec;$cmd;&$ret;" : execute.call(),
             "shell_exec;$cmd;" : shell_exec.call(),
             "system;$cmd;&$ret;" : system.call(),
             "passthru;$cmd;&$ret;" : passthru.call(),
             "popen;$cmd;" : popen.call(),
             }

FUNCTIONS2 = {
             "dl;" : "", 
             "escapeshellarg;" : "", 
             "escapeshellcmd;" : "", 
             "proc_close;" : "", 
             "proc_get_status;" : "", 
             "proc_nice;" : "", 
             "proc_open;" : "", 
             "proc_terminate;" : "",
             "shell_exec;" : "", 
             "system;" : "", 
             "checkdnsrr;" : "", 
             "closelog;" : "", 
             "define_syslog_variables;" : "", 
             "dns_check_record;" : "", 
             "dns_get_mx;" : "", 
             "dns_get_record;" : "", 
             "getenv;" : "", 
             "get_current_user;" : "", 
             "ini_get;" : "", 
             "php_uname;" : "", 
             "is_writable;" : "",
             "getcwd;" : "", 
             "getmyuid;" : "", 
             "getmygid;" : "", 
             "gethostbyaddr;" : "", 
             "gethostbyname;" : "", 
             "gethostbynamel;" : "", 
             "gethostname;" : "", 
             "getmxrr;" : "", 
             "getprotobyname;" : "", 
             "getprotobynumber;" : "", 
             "getservbyname;" : "", 
             "getservbyport;" : "", 
             "header_remove;" : "", 
             "header;" : "", 
             "headers_list;" : "", 
             "headers_sent;" : "", 
             "inet_ntop;" : "", 
             "inet_pton;" : "", 
             "ip2long;" : "", 
             "long2ip;" : "",
             "fclose;" : "", 
             "feof;" : "", 
             "fgets;" : "", 
             "fgetss;" : "", 
             "file;" : "", 
             "fopen;" : "", 
             "fsockopen;$hostname;$port;$errno;$errstr;$timeout;" : "", 
             "fwrite;" : "", 
             "mail;" : "", 
             "pfsockopen;" : "",
             "openlog;" : "", 
             "setcookie;" : "", 
             "setrawcookie;" : "", 
             "socket_recvfrom;" : "", 
             "socket_recv;" : "", 
             "stream_socket_recvfrom;" : "", 
             "msg_receive;" : "", 
             "socket_get_status;" : "", 
             "socket_set_blocking;" : "", 
             "socket_set_timeout;" : "", 
             "syslog;" : "", 
             "basename;" : "", 
             "chgrp;" : "", 
             "chmod;" : "", 
             "chown;" : "", 
             "clearstatcache;" : "", 
             "copy;" : "", 
             "dirname;" : "", 
             "disk_free_space;" : "36698988544", 
             "disk_total_space;" : "51221590016", 
             "diskfreespace;" : "36698988544", 
             "fclose;" : "", 
             "feof;" : "", 
             "fflush;" : "", 
             "fgetc;" : "", 
             "fgetcsv;" : "", 
             "fgets;" : "", 
             "fgetss;" : "", 
             "file_exists;" : "", 
             "file_get_contents;" : "", 
             "file_put_contents;" : "", 
             "file;" : "", 
             "fileatime;" : "", 
             "filectime;" : "", 
             "filegroup;" : "", 
             "fileinode;" : "", 
             "filemtime;" : "", 
             "fileowner;" : "", 
             "fileperms;" : "", 
             "filesize;" : "", 
             "filetype;" : "", 
             "flock;" : "", 
             "fnmatch;" : "", 
             "fopen;" : "", 
             "fpassthru;" : "", 
             "fputcsv;" : "", 
             "fputs;" : "", 
             "fread;" : "", 
             "fscanf;" : "", 
             "fseek;" : "", 
             "fstat;" : "", 
             "ftell;" : "", 
             "ftruncate;" : "", 
             "fwrite;" : "", 
             "glob;" : "", 
             "is_dir;" : "", 
             "is_executable;" : "", 
             "is_file;" : "", 
             "is_link;" : "", 
             "is_readable;" : "", 
             "is_uploaded_file;" : "", 
             "is_writable;" : "", 
             "is_writeable;" : "", 
             "lchgrp;" : "", 
             "lchown;" : "", 
             "link;" : "", 
             "linkinfo;" : "", 
             "lstat;" : "", 
             "mkdir;" : "", 
             "move_uploaded_file;" : "", 
             "parse_ini_file;" : "", 
             "parse_ini_string;" : "", 
             "pathinfo;" : "", 
             "pclose;" : "", 
             "popen;" : "", 
             "readfile;" : "", 
             "readlink;" : "", 
             "realpath_cache_get;" : "", 
             "realpath_cache_size;" : "", 
             "realpath;" : "", 
             "rename;" : "", 
             "rewind;" : "", 
             "rmdir;" : "", 
             "set_file_buffer;" : "", 
             "stat;" : "", 
             "symlink;" : "", 
             "tempnam;" : "", 
             "tmpfile;" : "", 
             "touch;" : "", 
             "umask;" : "", 
             "unlink;" : "", 
             }