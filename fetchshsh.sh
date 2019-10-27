ret=$(./bin/igetnonce 2>/dev/null | grep ECID)
ecidhex=$(echo $ret | cut -d '=' -f 2 )
ecidhex2=$(echo $ecidhex | tr '[:lower:]' '[:upper:]')
echo $ecidhex2 >/dev/null
ecid=$(echo "obase=10; ibase=16; $ecidhex2" | bc)
echo $ecid

ret=$(./bin/igetnonce 2>/dev/null | grep ApNonce)
nonce=$(echo $ret | cut -d '=' -f 2)
echo $nonce #APNONCE
mkdir ./shshtmp
./bin/tsschecker -e "$ecid" -d "iPhone6,1" -s -o -i 9.9.10.3.3 --buildid 14G60 -m firmware/buildmanifest.plist --save-path shshtmp/ --apnonce "$nonce"
mv ./shshtmp/* firmware/blobs.shsh
rm -rf ./shshtmp