#
class mysql::client (
  $bindings_enable = $mysql::params::bindings_enable,
  $package_ensure  = $mysql::params::client_package_ensure,
  $package_name    = $mysql::params::client_package_name,
  $iptables_allow  = hiera(client_nets)
) inherits mysql::params {

  include '::mysql::client::install'

  if !defined(iptables::add_tcp_stateful_listen['allow_mysql']){
    iptables::add_tcp_stateful_listen { 'allow_mysql':
      client_nets => $iptables_allow,
      dports      => $mysql::params::iptables_port
    }
  }

  if $bindings_enable {
    class { 'mysql::bindings':
      java_enable   => true,
      perl_enable   => true,
      php_enable    => true,
      python_enable => true,
      ruby_enable   => true,
    }
  }


  # Anchor pattern workaround to avoid resources of mysql::client::install to
  # "float off" outside mysql::client
  anchor { 'mysql::client::start': } ->
    Class['mysql::client::install'] ->
  anchor { 'mysql::client::end': }

}
