#a manifest that kills a process named

exec {'pkill killmenow':
    path     => '/user/bin',
    command  => 'pkill killmenow',
    provider => shell, 
    returns  => [0, 1],
}
