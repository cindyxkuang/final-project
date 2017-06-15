# Mapping the alternative fuel stations of the U.S. (https://alt-fuel-stations-map.herokuapp.com/)

## Elevator Pitch

I was interested in looking at climate data, especially given the current administration's track record on environmental policy. In doing research, I happened to find an API for a dataset of all the registered alternative fuel stations (AFS) in the U.S. Although the API itself offers extremely thorough information on each individual station, I was interested in visually plotting each station on a comprehensive map, as well as offering search functionality for a user intending to find local AFS.

## Inspirations & Prior Work

**1. [Walking in L.A.: Times analysis finds the county's 817 most dangerous intersections]
(http://graphics.latimes.com/la-pedestrians/), via L.A. Times**

This article maps and analyzes the number of pedestrian-involved traffic accidents at a number of intersections in L.A., determining several "danger zones" where accidenters are most frequent. It uses Leaflet to develop interactive maps of the geocoded accident locations. When developing my own app, I will be using Leaflet to efficiently geocode station locations. However, due to the volume of my data, I will most likely be unable to perform analysis to the same amount of detail as the Times did.
* The scope of this project is much smaller than my app's. I will have to consider how to feasibly represent the fuel stations on a map without overcrowding (since there are over 28,000 data points).
* Using a visual representation and geocoding data appears to be an effective way to depict complicated data in a user-friendly way. I will be doing this for my project.

**2. [Estimated % of adults who think global warming is happening, 2016]
(http://climatecommunication.yale.edu/visualizations-data/ycom-us-2016/), via Yale Program on Climate Change Communication**

I thought this article did an effective job of presenting a large dataset in a manner that is comprehensible with the first look. The percentages of adults who believed in global warming were broken down by county, so it was extremely apparent where the believers and the non-believers were concentrated, respectively. That being said, I think breaking up such a big data set into such microscopic levels has its drawbacks, specifically in its lacking of summarization of the data. I want to implement the interactivity of this map in my own project, and perhaps I will color-code the markers in my map to correspond with the fuel type offered there.
* The filtering function on this project was essential for helping to understand the data. Since I have only a few days to implement this map, I will allow geographic filtering.
* The different answers given to open-ended questions like "Do you believe global warming exists?" are much more difficult to encode than the geocoded data of alternative fuel stations. If I have time, I think it would be valuable to visually represent the types of fuel offered at each station as well.

**3. [How Uber Uses Psychological Tricks to Push Its Drivers’ Buttons]
(https://www.nytimes.com/interactive/2017/04/02/technology/uber-drivers-psychological-tricks.html), via The New York Times**

This article investigates the way Uber leverages its driver-rider-matching algorithm to decrease perceived wait time at the expense of drivers. It exposed the inner workings of Uber, creating yet another public relations crisis for the company in the midst of several allegations of sexual harrassment and sexism in its workplace environment. The article also includes one of the most interesting visualizations I've ever seen. Allowing users to toggle through the different scenarios of driver to rider ratios was a very visually aesthetic way to represent data. 
* While the visualization was very nice to look at, the perpetual motion of everything in it made it difficult to concentrate on any one thing at a time. I think allowing user interaction is a net positive, but keeping things simple for the user is also important. I will allow the user to interact with the map through filtering functionality as well as repositioning/resizing, but will also present the data in a static data table.

## Articles

**1. [Western Washington Clean Cities Tout Alt-Fuel Vehicle Fleets]
(https://ngtnews.com/western-washington-clean-cities-touts-alt-fuel-vehicle-fleets), via Next-Gen Transportation News**
When we consider alternative fuel vehicles (AFVs), the first thing that comes to mind is usually private vehicles used by the average consumer. However, a significant portion of government-owned vehicles actually run on alt fuels, and these fleets need charging stations. It would be interesting to look at the location and numbers of government-owned fuel stations.

**2. [First Came the Hydrogen Cars. Now, the Refueling Stations.]
(https://www.nytimes.com/2017/05/18/automobiles/wheels/first-came-the-hydrogen-cars-now-the-refilling-stations.html?rref=collection%2Ftimestopic%2FAlternative%20Fuel%20Vehicles&action=click&contentCollection=timestopics&region=stream&module=stream_unit&version=latest&contentPlacement=3&pgtype=collection), via The New York Times**
Hydrogen fuel cell-powered cars are a new technology and are currently only available in California. As a result, it is reasonable to assume that the number of hydrogen-servicing fueling stations are scarce. This article examines the rise of hydrogen cars and the subsequent appearance of the necessary infrastructure.

**3. [2017 Could Prove to Be a Turning Point for Plug-in Hybrids]
(https://www.nytimes.com/2017/05/04/automobiles/wheels/plug-in-electric-hybrid-automobiles.html?rref=collection%2Ftimestopic%2FAlternative%20Fuel%20Vehicles&action=click&contentCollection=timestopics&region=stream&module=stream_unit&version=latest&contentPlacement=6&pgtype=collection), via The New York Times**
This article covers electric-gasoline hybrid cars as a cost-efficient option for alt-fuel vehicles. As data on fueling stations will show, about half of the charging stations in the nation are privately owned. It would be interesting to utilize this data to inquire into how a private fueling station comes to be and what legal implications surround it.

## Data
My data comes from the National Renewable Energy Laboratory, which is a lab of the U.S. Department of Energy. I utilized their Alternative Fuel Stations API both to collect an initial sampling of fuel stations for my homepage and to implement the filtering features of my app.

## Deployment
I deployed this app on Heroku.
