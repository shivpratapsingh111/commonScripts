### nuclei
* Script to organise nuclei templates: https://github.com/shivpratapsingh111/organiseNuclei

### scriptsReconftw
* scriptsReconftw/ dir contains scripts related to ReconFTW tool, to organize.
    * ssClassify/ - This folder contains all the necessary files and code to classify scrrenshots based on their category. (Sub-Module of `organise.sh`)
    * organise.sh - organises ReconFTW Output data.
    * checkAllowedMethods.sh - sends request in POST and OPTIONS method to every subdomain having screenshot stored in `methodNotAllowed/` dir (`methodNotAllowed/` dir contains screenshots of all subdomains giving `status code 405` (Method Not Allowed) and stores the response in `allResponses.txt`. You get this dir after using `organise.sh` which classifies screenshots based on their category)
    * getUrlFromName.sh - gives you url by replacing `-` (underscores) with `/` (forward slashes) in the screenshot name taken by ReconFTW 

### server
* server/ dir contains scripts related to server upload and download.
    * download.sh - downloads file from server using scp utility.
    * upload.sh - uploads file to server using scp utility.
    * syncFolder.sh - syncs server & client folder.

