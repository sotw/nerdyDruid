INSFOLDER=~/.nerdyDruid
echo "Nerd + Plant = nerdyDruid, you are welcome to nerdyDruid brotherhood."
rm -Rf $INSFOLDER
rm -f ~/bin/sh/nerdyDruid
mkdir -p ~/bin/sh
mkdir -p $INSFOLDER
cp nerdyDruid ~/bin/sh
cp *.py $INSFOLDER
cp *.db $INSFOLDER
chmod -R 755 $INSFOLDER
chmod -R 755 ~/bin/sh

echo "Do you want to add PATH envirnment in .bashrc?(restart terminal will effect at once)"
select yn in "Yes" "No"; do
	case $yn in
		Yes ) echo "PATH=$PATH:~/bin/sh:~/bin" > ~/.bashrc; break;;
	    No ) google have a green day; break;;
	esac
done
