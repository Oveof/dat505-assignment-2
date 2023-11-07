
{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    nativeBuildInputs = with pkgs.buildPackages; [ 
      # python311
      (python311.withPackages(ps: with ps; [ 
        scapy
        # mininet
      ]))
      mininet
      openvswitch
      service-wrapper
      python311Packages.mininet-python
      python-launcher
      python311Packages.pip
      python311Packages.python-lsp-server
    ];
}

# with import <nixpkgs> {};
# (python311.withPackages (ps: with ps; [
#   scapy
#   mininet
# ])).env