import csv
import numpy as np
import os
from string import Template


# Parse the data file
string = open('data.csv','r').read().replace('\xc2','').replace('\xa0','').replace('\xc3','').replace('\xe3','').replace('\xe3','')

# Obtain package names
rows = string.split('\n')
packages = rows[0].split(';')[1:]
packages = [str(p).replace('"','') for p in packages]

#Obtain attributes
attrs = []
for i, row in enumerate(rows):
    if i == 0:
        pass
    else:
        attrs.append(row.split(';')[0].replace('"',''))
attrs.reverse()
attrs = attrs[1:]

# Obtain 'inner data' and flip it upside down
rows = rows[1:-1]
outer = []
for row in rows:
    row = row.split(';')
    row = [r.replace('"','') for r in row]
    outer.append(row)
data = np.array(outer)
data = np.flipud(data)
data = data[:,1:]

# Obtain git repos
temp = rows[1].split(';')[1:]
temp = [t.replace('"','') for t in temp]
repos = dict(zip(packages,temp))

# The templates
package_template = Template("""  { "fields" :
      { "category" : 1,
        "modified": "2010-01-01 12:00:00",
        "created": "2010-01-01 12:00:00",
        "participants" : "",
        "pypi_downloads" : 0,
        "pypi_url" : "",
        "related_packages" : [],
        "repo_commits" : 0,
        "repo_description" : "$repo_description",
        "repo_forks" : 0,
        "repo_url" : "$repo_url",
        "repo_watchers" : 0,
        "slug": "$title",
        "title": "$title"
      },
    "model" : "package.package",
    "pk" : $pk
  },\n""")

gridpackage = Template("""  { "fields" :
      { "created" : "2010-01-01 12:00:00",
        "grid" : 1,
        "modified" : "2010-01-01 12:00:00",
        "package" : $package
      },
    "model" : "grid.gridpackage",
    "pk" : $pk
  },\n""")

feature = Template("""  { "fields" :
      { "created" : "2010-01-01 12:00:00",
        "description" : "$title",
        "grid" : 1,
        "modified" : "2010-01-01 12:00:00",
        "title" : "$title"
      },
    "model" : "grid.feature",
    "pk" : $pk
  },\n""")

element  =   Template("""  { "fields" :
      { "created" : "2010-01-01 12:00:00",
        "feature" : $feature,
        "grid_package" : $grid_package,
        "modified" : "2010-01-01 12:00:00",
        "text" : "$text"
      },
    "model" : "grid.element",
    "pk" : $pk
  },\n""")


descript_dict = {}
descript_dict['dhtmlxChart'] = """Elycharts is a pure javascript charting library, easy to use and completely customizable.  It helps you create good looking interactive charts on you web pages or web applications, with a lot of useful features: legend and label support, mouse tracking, tooltips, templates and animations."""
descript_dict['Dygraphs'] = """dygraphs is an open source JavaScript library that produces produces interactive, zoomable charts of time series. It is designed to display dense data sets and enable users to explore and interpret them."""
descript_dict['Elycharts'] = """Elycharts is a pure javascript charting library, easy to use and completely customizable.  It helps you create good looking interactive charts on you web pages or web applications, with a lot of useful features: legend and label support, mouse tracking, tooltips, templates, and animations."""
descript_dict['gRaphael'] = """gRaphael's goal is to help you create stunning charts on your website."""
descript_dict['Highcharts'] = """Highcharts is a charting library written in pure JavaScript, offering an easy way of adding interactive charts to your web site or web application. Highcharts currently supports line, spline, area, areaspline, column, bar, pie and scatter chart types.  It works in all modern browsers including the iPhone/iPad and Internet Explorer from version 6. Standard browsers use SVG for the graphics rendering. In Internet Explorer graphics are drawn using VML."""
descript_dict['JIT'] = """The JavaScript InfoVis Toolkit provides tools for creating Interactive Data Visualizations for the Web."""
descript_dict['JSCharts'] = """JS Charts is a JavaScript based chart generator that requires little or no coding. With JS Charts drawing charts is a simple and easy task, since you only have to use client-side scripting (i.e. performed by your web browser). No additional plugins or server modules are required. Just include our scripts, prepare your chart data in XML, JSON or JavaScript Array and your chart is ready!"""
descript_dict['JSXGraph'] = """JSXGraph is a cross-browser library for interactive geometry, function plotting, charting, and data visualization in a web browser. It is implemented completely in JavaScript, does not rely on any other library, and uses SVG, VML, or canvas."""
descript_dict['Protovis'] = """Protovis composes custom views of data with simple marks such as bars and dots. Unlike low-level graphics libraries that quickly become tedious for visualization, Protovis defines marks through dynamic properties that encode data, allowing inheritance, scales and layouts to simplify construction."""
descript_dict['GoogleCharts'] = """The Google Chart API returns a chart image in response to a URL GET or POST request. The API can generate many kinds of charts, from pie or line charts to QR codes and formulas. All the information about the chart that you want, such as chart data, size, colors, and labels, are part of the URL."""
descript_dict['d3'] = """D3.js is a small, free JavaScript library for manipulating documents based on data."""


# Inserting data into the templates
ofile = open('debug.json', 'w')
for i, package in enumerate(packages):
    if len(repos[package]) >= 4:
        ofile.write(package_template.substitute(pk=i+1, title=package, repo_description = descript_dict[package], repo_url=repos[package]))
    else:
        ofile.write(package_template.substitute(pk=i+1, title=package, repo_description = descript_dict[package], repo_url=i+1))
    ofile.write(gridpackage.substitute(pk=i+1, package=i+1))
for i, attr in enumerate(attrs):
    ofile.write(feature.substitute(pk=i+1, title=attr))

pk = 0
for j, attr in enumerate(attrs):
    for i, package in enumerate(packages):
        pk += 1
        if j == len(attrs) - 1 and i == len(packages) - 1:
            temp = element.substitute(feature=j+1, grid_package=i+1, text=str(data[j,i]), pk=pk)
            temp = temp[0:-2]
            temp = temp + '\n'
            ofile.write(temp)
        else:
            ofile.write(element.substitute(feature=j+1, grid_package=i+1, text=str(data[j,i]), pk=pk))
ofile.write(']')
ofile.close()

# TODO; Don't use the OS to do this
os.system("cat basics.json > initial_data.json")
os.system("cat debug.json >> initial_data.json")
os.unlink('debug.json')
