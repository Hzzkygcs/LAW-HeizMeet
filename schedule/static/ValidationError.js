class ValidationError extends Error{
    constructor(message) {
      alert(message);
      super(message);
      this.name = this.constructor.name;

    }
}