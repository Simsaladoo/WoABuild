// Login to SynologyNAS via SSH steps:


1. open cmd and type: 
ssh Simsaladoo@192.168.50.146 -p22

2. enter pw:
POIU)(*&poiu0987

3. navigate to p4 exe
-can enter dir, hit enter, to see the folder structure
cd /volume1/SimNAS/OneDrive/Perforce

4. set Linux permissions on p4 and p4d applications
chmod +x p4
chmod +x p4d

5. List any currently running process named 'p4d'
ps | grep p4d

6. If 5 is false, start p4d with this -r command:
/volume1/SimNAS/OneDrive/Perforce/p4d -r /volume1/SimNAS/p4root



// Jenkins on SynologyNAS
// https://www.gdcorner.com/2019/12/27/JenkinsHomeLab-P1-MasterSetup.html#running-the-jenkins-docker-image-from-a-synology-nas

1. setup the folder & its permissions:
sudo chown -R 1000:1000 /volume1/SimNAS/InProd/WoA/Jenkins/data

2. Initial SSH Setup:
cat /data/secrets/initialAdminPassword

3. Copy the outputted key:
89d1ca934e7e496c94133213fc9c013a

4. Find the Local Port used by the Agent:8080 Port, which will become the login port
http://192.168.50.146:49162

5. SimNAS Jenkins login info:
Simkins
p00pie

6. Spin up a Jenkins Agent on the NAS:
docker run -d --rm --name=Simkins_Agent -p 4444:22 -e "JENKINS_AGENT_SSH_PUBKEY=ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDebgLiV7DoflaSHjfjnL9VkvPOKrzuq3Ow6OLEYsJ1jsYbofY2B5yn/mbHZFZZyx/gv4bnl+Z1FU7hHZnRtRgqLT6NerFnGloBLVjxIMnnJ0hTFrwaw3g1azU8DbLx3HyaSq194eiOVWU+D+XomjIogBrSmxJTJmmZ2CCsMsavTNYMM0QJwosQHuZmEDP3wfTwrO+rWF4y6h+gGMB2jd0GswKjdV3LCDYfogCg87oPAFCKC4A4b5ayFviMBpW4MswgnnSp5MzFZBmSFf52moo6SQNBIzWACtjKj3RMZKN9d0dvAELBBmUAzuOCPoxuneDbcX1qFS2R6IZFppxpMvbpl34nucmPFg2rrGTN5NzFefsiAfJG15eEKyUkLcpsOE56I9r9osdhjlV3zgnMHVaSmYA+qxcR2mRLl+6ViIVHew29g7RxUlPjy5JDCva6IV+Ijsirt2TDm0BDuKemm/IRjsIUH0ZJynjukndpWuL2h16VBQ8RvGfX+ynMCA+O18M= Simsaladoo@SimNAS" jenkins/ssh-agent:alpine-jdk17

