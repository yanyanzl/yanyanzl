# Securities basics


### What is SSH?

1. SSH or Secure Shell is a network communication protocol that enables two computers to communicate (c.f http or hypertext transfer protocol, which is the protocol used to transfer hypertext such as web pages) and share data. An inherent feature of ssh is that the communication between the two computers is encrypted meaning that it is suitable for use on insecure networks.

2. SSH is often used to "login" and perform operations on remote computers but it may also be used for transferring data.

3. You use a program on your computer (ssh client), to connect to a SSH server and transfer the data to/from our storage using either a graphical user interface or command line

4. Secure Shell provides strong password authentication and public key authentication, as well as encrypted data communications between two computers connecting over an open network, such as the internet.

5. SSH is widely used by network administrators to manage systems and applications remotely, enabling them to log in to another computer over a network, execute commands and move files from one computer to another, including secure remote access to resources, remote execution of commands, delivery of software patches, and updates and other administrative or management tasks.

6. SSH also replaces file transfer programs, such as File Transfer Protocol (FTP) and rcp (remote copy).

7. SSH is used to manage routers, server hardware, virtualization platforms, operating systems (OSes), and inside systems management and file transfer applications.

### how to be a SSH server
- Set up Remote Login on your Mac
    - On your Mac, choose Apple menu  > System Settings, click General  in the sidebar, then click Sharing on the right. (You may need to scroll down.)

    - Turn on Remote Login, then click the Info button  on the right.

    - If you want, turn on “Allow full disk access for remote users.”
    
- Configuration of the SSH Server
    - under /etc/ssh/
    - Open the SSH configuration file sshd_config with the text editor vi: vi /etc/ssh/sshd_config.

    
### Log in to your Mac from another computer
- On the other computer, open the Terminal app  (if it’s a Mac) or an SSH client.

- Type the ssh command, then press Return.
    - ssh username@hostname
    The hostname can be an IP address or a domain name. : ssh steve@10.1.2.3
    
- select yes to continue. and input your remote server users password. you are in a remote terminal now.

- the first time connection will permanently add hostname to the list of known hosts.


- set up public key authentication (passwordless SSH login. so to be more secure)
    - on your SSH client computer. open terminal
    - Check for Existing SSH Keys: ls -al ~/.ssh/id_*.pub
    - Generate SSH Key Pair if not yet. : ssh-keygen -t ed25519 -C "your_email@example.com"
    - Copy the key to the remote Server by command (replace id_ed25519.pub with your public key file name): ssh-copy-id -i ~/.ssh/id_ed25519.pub user@host
        - i Specifies the identity file that is to be copied (default is ~/.ssh/id_rsa). If this option is not provided, this adds all keys listed by ssh-add -L. Note: it can be multiple keys and adding extra authorized keys can easily happen accidentally! If ssh-add -L returns no keys, then the most recently modified key matching ~/.ssh/id*.pub, excluding those matching ~/.ssh/*-cert.pub, will be used.

### close the SSH connection
- To disconnect from the server and close the SSH connection, simply type "exit" and press the Enter key


### OpenSSL

1. OpenSSL is a software library for applications that provide secure communications over computer networks against eavesdropping, and identify the party at the other end. It is widely used by Internet servers, including the majority of HTTPS websites.

2. OpenSSL contains an open-source implementation of the SSL and TLS protocols. The core library, written in the C programming language, implements basic cryptographic functions and provides various utility functions. Wrappers allowing the use of the OpenSSL library in a variety of computer languages are available.

3. OpenSSL supports a number of different cryptographic algorithms:

    - Ciphers
        - AES, Blowfish, Camellia, Chacha20, Poly1305, SEED, CAST-128, DES, IDEA, RC2, RC4, RC5, Triple DES, GOST 28147-89, SM4
    
    - Cryptographic hash functions
        - MD5, MD4, MD2, SHA-1, SHA-2, SHA-3, RIPEMD-160, MDC-2, GOST R 34.11-94, BLAKE2, Whirlpool, SM3
    
    - Public-key cryptography
        - RSA, DSA, Diffie–Hellman key exchange, Elliptic curve, X25519, Ed25519, X448, Ed448, GOST R 34.10-2001,SM2
        
        