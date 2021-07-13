# sphinx
function build_docs {
	cd $DIR/docs
	make clean html
	cd -
}
