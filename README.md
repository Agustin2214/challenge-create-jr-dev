### BACK:

1. Crea un entorno virtual.
2. El proyecto inicia con el index, puede tener errores al iniciar. **SOLUCIONAR**.

3. Al crear un nuevo contacto, validar que el email utilizado no pueda volver a ser utilizado. Modificar el endpoint ya creado. La aplicación no debe romper; capturar errores.

4. Crear un endpoint para buscar contacto por ID.

5. Los endpoints de actualizar y eliminar no funcionan por algún motivo. **Solucionar**.

6. Crear un endpoint de búsqueda por nombre.


7. **PLUS**: Dejar para el último; agregar try-except a todos los endpoints.


**PISTA**
    Para eliminar debe ser por id en el front quizas no llegue esa informacion. Modificar el endpoint del get para que traiga esa info


### Front:
- Actualmente se renderiza un lista de contact.
- Al lado de cada nombre de contacto debe aparecer una "x" para eliminar.

- Agregar un input con un botón "crear" que cree nuevos contactos.

- Al hacer clic en un contacto, llevarlo a un detalle (`/id` -> nueva vista) donde se muestren nombre, email y teléfono, y que sean editables.
- Agregar un buscador al inicio para filtrar.
- Debe ser un SPA (Single Page Application); no se puede recargar la página.
- Después de finalizar, dar la mejor calidad de estilo, a su propio gusto. Utilizar el resto del tiempo para esto.
