# Mapping the alternative fuel stations of the U.S. (https://alt-fuel-stations-map.herokuapp.com/)

## Elevator Pitch

I was interested in looking at climate data, especially given the current administration's track record on environmental policy. In doing research, I happened to find an API for a dataset of all the registered alternative fuel stations (AFS) in the U.S. Although the API itself offers extremely thorough information on each individual station, I was interested in visually plotting each station on a comprehensive map, as well as offering search functionality for a user intending to find local AFS.

## Inspirations & Prior Work

**1. [Walking in L.A.: Times analysis finds the county's 817 most dangerous intersections]
(http://graphics.latimes.com/la-pedestrians/), via L.A. Times**

This article maps and analyzes the number of pedestrian-involved traffic accidents at a number of intersections in L.A., determining several "danger zones" where accidenters are most frequent. It uses Leaflet to develop interactive maps of the geocoded accident locations. When developing my own app, I will be using Leaflet to efficiently geocode station locations. However, due to the volume of my data, I will most likely be unable to perform analysis to the same amount of detail as the Times did.

**2. [Estimated % of adults who think global warming is happening, 2016]
(http://climatecommunication.yale.edu/visualizations-data/ycom-us-2016/), via Yale Program on Climate Change Communication**

I thought this article did an effective job of presenting a large dataset in a manner that is comprehensible with the first look. The percentages of adults who believed in global warming were broken down by county, so it was extremely apparent where the believers and the non-believers were concentrated, respectively. That being said, I think breaking up such a big data set into such microscopic levels has its drawbacks, specifically in its lacking of summarization of the data. I want to implement the interactivity of this map in my own project, and perhaps I will color-code the markers in my map to correspond with the fuel type offered there.

## Data
My data comes from the National Renewable Energy Laboratory, which is a lab of the U.S. Department of Energy. I utilized their Alternative Fuel Stations API both to collect an initial sampling of fuel stations for my homepage and to implement the filtering features of my app.

## Deployment
I deployed this app on Heroku.
