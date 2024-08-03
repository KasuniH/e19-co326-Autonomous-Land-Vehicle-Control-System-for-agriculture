# FIXME: before you push into master...
RUNTIMEDIR=C:/Program Files/OpenModelica1.22.3-64bit/include/omc/c/
#COPY_RUNTIMEFILES=$(FMI_ME_OBJS:%= && (OMCFILE=% && cp $(RUNTIMEDIR)/$$OMCFILE.c $$OMCFILE.c))

fmu:
	rm -f VehicleDynamics.fmutmp/sources/VehicleDynamics_init.xml
	cp -a "C:/Program Files/OpenModelica1.22.3-64bit/share/omc/runtime/c/fmi/buildproject/"* VehicleDynamics.fmutmp/sources
	cp -a VehicleDynamics_FMU.libs VehicleDynamics.fmutmp/sources/

