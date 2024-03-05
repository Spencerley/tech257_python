# SSH

## What is it?

- SSH or Secure Shell is a network communication protocol that enables two computers to communicate (c.f http or hypertext transfer protocol, which is the protocol used to transfer hypertext such as web pages) and share data.

## What does it stand for?

- Secure Shell

## Why use it over HTTPS?

- SSH is more secure than entering credentials over HTTPS, it is recommended for businesses dealing with sensitive and critical data. Once you generate the SSH keys, only the machines with the key file on disk can access the repository.

## How do you create an SSH key pair?

- Using the ssh-keygen command
- `ssh-keygen -t rsa -f C:\Users\WINDOWS_USER\.ssh\KEY_FILENAME -C USERNAME -b 2048`
- Replace the following:
  - WINDOWS_USER: your username on the Windows machine. 
  - KEY_FILENAME: the name for your SSH key file. For example, a filename of my-ssh-key generates a private key file named my-ssh-key and a public key file named my-ssh-key.pub. 
  - USERNAME: your username on the VM. For example, cloudysanfrancisco, or cloudysanfrancisco_gmail_com. 
  - For Linux VMs, the USERNAME can't be root, unless you configure your VM to allow root login. For more information, see Connect to VMs as the root user. 
  - For Windows VMs that use Active Directory (AD), the username must be prepended with the AD domain, in the format of DOMAIN\. For example, the user cloudysanfrancisco within the ad.example.com AD has a USERNAME of example\cloudysanfrancisco.
- i.e. `ssh-keygen -t rsa -b 4096 -C "<your_email_here>"`

## What are some best practices when using/implementing SSH?

- Maintain an Accurate Inventory of Keys (and Disable Old Ones)
  - If old keys are not deleted they will remain active on the device until expressly deleted.
- Maintain a Current Whitelist of Authorized Users
  - Previous users could still access the organization’s servers remotely, even after their contract was terminated, if the certificates were installed on devices that they continued to have access to.
- Only Grant Access to Essential Authorized Users
  - You should always restrict how much access should be provided to each user based on what they need to access.
- Assign Key Management Duties to Specific People
  - SSH keys can be generated easily using simple commands. This advantage can quickly transform into a disadvantage if carried out by someone with bad intentions or ill-gotten access.
- Use a Reliable SSH Key Manager
  - This will allow you to automate some of the functions otherwise performed manually.
- Rotate SSH Keys
  - Replace your organization’s old SSH keys with new ones. This process should be carried out regularly in every organization to minimize risks.
- Define an Invalidation Term for Your SSH Keys
  - ensure that all keys belonging to employees who leave the organization should be deleted — or, at the very least, invalidated — on the spot.
- Use Updated Versions of the SSH Protocol
  - When the SSH protocol is not updated to its latest version, you make yourself vulnerable to cyberattacks.
<br>
</br>
- cat public key `cat [file name]`
- Put key on GitHub (not a command) - go to security, deploy key, add new key, give it a title and copy the public key in below.
- Create ssh-agent process - `eval ssh-agent` 
- Add ssh key to ssh-agent `ssh-add <path to key>`
- Test connection to GitHub - `ssh -T git@github.com`