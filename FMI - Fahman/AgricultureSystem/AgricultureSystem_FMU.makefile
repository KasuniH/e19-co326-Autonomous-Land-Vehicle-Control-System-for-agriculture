# FIXME: before you push into master...
RUNTIMEDIR=C:/Program Files/OpenModelica1.22.3-64bit/include/omc/c/
#COPY_RUNTIMEFILES=$(FMI_ME_OBJS:%= && (OMCFILE=% && cp $(RUNTIMEDIR)/$$OMCFILE.c $$OMCFILE.c))

fmu:
	rm -f AgricultureSystem.fmutmp/sources/AgricultureSystem_init.xml
	cp -a "C:/Program Files/OpenModelica1.22.3-64bit/share/omc/runtime/c/fmi/buildproject/"* AgricultureSystem.fmutmp/sources
	cp -a AgricultureSystem_FMU.libs AgricultureSystem.fmutmp/sources/

