let orbitToSatellites = {};

if (orbitToSatellites.hasOwnProperty(sat.orbitID)) {
  orbitToSatellites[sat.orbitID].push(sat);
} else {
  orbitToSatellites[sat.orbitID] = [sat];
}