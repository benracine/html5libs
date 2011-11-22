echo 'dumping grid.grid'
heroku run --app html5libs python opencomparison/manage.py dumpdata grid.grid --indent=2 > ../clone2/opencomparison/fixtures/grid.json
fromdos ../clone2/opencomparison/fixtures/grid.json
sed -i '1d' ../clone2/opencomparison/fixtures/grid.json

echo 'dumping auth.user'
heroku run --app html5libs python opencomparison/manage.py dumpdata grid.grid --indent=2 > ../clone2/opencomparison/fixtures/user.json
fromdos ../clone2/opencomparison/fixtures/user.json
sed -i '1d' ../clone2/opencomparison/fixtures/user.json

echo 'dumping grid.gridpackage'
heroku run --app html5libs python opencomparison/manage.py dumpdata grid.gridpackage --indent=2 > ../clone2/opencomparison/fixtures/gridpackage.json
fromdos ../clone2/opencomparison/fixtures/gridpackage.json
sed -i '1d' ../clone2/opencomparison/fixtures/gridpackage.json

echo 'dumping grid.feature'
heroku run --app html5libs python opencomparison/manage.py dumpdata grid.feature --indent=2 > ../clone2/opencomparison/fixtures/feature.json
fromdos ../clone2/opencomparison/fixtures/feature.json
sed -i '1d' ../clone2/opencomparison/fixtures/feature.json

echo 'dumping grid.element'
heroku run --app html5libs python opencomparison/manage.py dumpdata grid.element --indent=2 > ../clone2/opencomparison/fixtures/element.json
fromdos ../clone2/opencomparison/fixtures/element.json
sed -i '1d' ../clone2/opencomparison/fixtures/element.json

echo 'dumping package.package'
heroku run --app html5libs python opencomparison/manage.py dumpdata package.package --indent=2 > ../clone2/opencomparison/fixtures/package.json
fromdos ../clone2/opencomparison/fixtures/package.json
sed -i '1d' ../clone2/opencomparison/fixtures/package.json

echo 'dumping everything'
heroku run --app html5libs python opencomparison/manage.py dumpdata --indent=2 > ../clone2/opencomparison/fixtures/everything.json
fromdos ../clone2/opencomparison/fixtures/everything.json
sed -i '1d' ../clone2/opencomparison/fixtures/everything.json
